"""Package existing result tables for Overleaf without loading scores or models."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import zipfile


ROOT = Path(__file__).resolve().parents[1]
DATASETS = {"imdb": "IMDb", "dblp": "DBLP"}
TASKS = {"movie_year": "Movie--Year", "movie_director": "Movie--Director",
         "paper_conference": "Paper--Conference"}
CLASS_COLUMNS = (("accuracy", "Accuracy"), ("precision_macro", "Precision"),
                 ("recall_macro", "Recall"), ("micro_f1", "Micro-F1"), ("macro_f1", "Macro-F1"))
PAIR_COLUMNS = (("prediction_agreement", "Agreement@1"), ("tau_b", r"Kendall-$\tau_b$"))
LP_COLUMNS = (("mrr", "MRR"), ("hits@1", "Hits@1"), ("hits@3", "Hits@3"), ("hits@10", "Hits@10"))


def latex_escape(value):
    return str(value).replace("&", r"\&").replace("_", r"\_").replace("%", r"\%")


def metric_cell(value):
    estimate, error = value["estimate"], value["bootstrap_se"]
    if error is None:
        return f"${estimate:.4f}$"
    return f"${estimate:.4f} \\pm {error:.4f}$"


def grid_table(headers, rows, caption, label):
    row_end = " " + chr(92) * 2
    lines = ["% Requires adjustbox.", r"\begin{table}[htbp]", r"\centering", r"\small",
             r"\renewcommand{\arraystretch}{1.15}", r"\setlength{\tabcolsep}{5pt}",
             r"\begin{adjustbox}{max width=\linewidth}",
             "\\begin{tabular}{|" + "|".join("l" for _ in headers) + "|}", r"\hline",
             " & ".join(r"\textbf{" + name + "}" for name in headers) + row_end, r"\hline"]
    for row in rows:
        lines.extend([" & ".join(row) + row_end, r"\hline"])
    lines.extend([r"\end{tabular}", r"\end{adjustbox}",
                  "\\caption{" + caption + "}", "\\label{" + label + "}", r"\end{table}", ""])
    return "\n".join(lines)


def presentation_table(record, dataset, task, kind, bootstrap):
    physical = sorted((name.split("/", 1)[1], result)
                      for name, result in record["performance"].items() if name.startswith("physical/"))
    if not physical:
        raise ValueError(f"No physical variants in {dataset}/{task}")
    contract = record["comparison_contract"]
    stage = contract.get("evaluation_stage", "zeroshot")
    method = latex_escape(contract["model"] + (" (FT)" if stage == "finetuned" else ""))
    dataset_name = DATASETS[dataset]
    task_name = TASKS[task]
    queries = physical[0][1]["num_queries"]
    classes = physical[0][1]["classification_classes"]
    label = f"tab:motif-{dataset}-{task.replace('_', '-')}-{kind}"
    setting = "fine-tuned" if stage == "finetuned" else "zero-shot"
    context = f"Preliminary {setting} MOTIF results on {dataset_name} {task_name}; {queries:,} {contract['split']} queries. "
    if stage == "finetuned":
        trained = contract["fine_tuning"]["training_contract"]
        context += f"Fine-tuned on variant {latex_escape(trained['train_variant'])}; checkpoint selected by validation MRR. "
    uncertainty = (f"Values are estimates $\\pm$ bootstrap standard error ({bootstrap:,} query resamples)."
                   if bootstrap else "Values are point estimates.")
    if kind == "invariance":
        headers = ["Method", "Comparison"] + [name for _, name in PAIR_COLUMNS]
        rows = [[method, latex_escape(name)] + [metric_cell(result["metrics"][key]) for key, _ in PAIR_COLUMNS]
                for name, result in sorted(record["physical_pairs"].items())]
        caption = (context + "Variant comparisons use the same 20 candidates per query. "
                   "Agreement@1 compares predictions; Kendall tau-b compares rankings within each query. " + uncertainty)
    else:
        columns = CLASS_COLUMNS if kind == "classification" else LP_COLUMNS
        headers = ["Dataset", "Method", "Variant"] + [name for _, name in columns]
        rows = [[dataset_name, method, latex_escape(variant)] +
                [metric_cell(result["metrics"][key]) for key, _ in columns] for variant, result in physical]
        protocol = (f"Classification over all {classes:,} target classes; precision and recall are macro-averaged. "
                    if kind == "classification" else
                    "Tail-only link prediction over the original 20 candidates; score ties use average rank. ")
        caption = context + protocol + uncertainty
    return grid_table(headers, rows, caption, label)


def matrix_tables(summary, include_lp=False):
    """Render saved train/test statistics; no score loading or metric recomputation."""
    variants = summary["variants"]
    task, dataset = summary["task"], summary["dataset"]
    method = "MOTIF (FT)"
    first = summary["cells"][variants[0]][variants[0]]
    context = (f"Preliminary fine-tuned MOTIF on {DATASETS[dataset]} {TASKS[task]}; "
               f"seed {summary['seed']}, {first['num_queries']:,} {summary['split']} queries. ")
    trained = summary["shared_training_contract"]
    context += f"Each variant uses {trained['steps']:,} optimizer steps; validation MRR selects its checkpoint. "
    if trained["val_limit"] or summary["shared_evaluation_contract"]["limit"]:
        context += "Limited-query debugging run. "
    uncertainty = (f"Values are estimates $\\pm$ query-bootstrap standard error "
                   f"({summary['bootstrap']:,} resamples), not variation across training seeds."
                   if summary["bootstrap"] else "Values are point estimates.")
    prefix = f"tab:motif-{dataset}-{task.replace('_', '-')}-matrix"
    files = {}
    protocol = (f"Classification uses all {first['classification_classes']:,} target classes; "
                "precision and recall are macro-averaged. ")
    for kind, columns in (("classification", CLASS_COLUMNS), ("link_prediction", LP_COLUMNS)):
        if kind == "link_prediction" and not include_lp:
            continue
        notes = protocol if kind == "classification" else "LP ranks the original 20 candidates with average ranks for ties. "
        diagonal = [[DATASETS[dataset], method, variant] +
                    [metric_cell(summary["cells"][variant][variant]["metrics"][key]) for key, _ in columns]
                    for variant in variants]
        files[kind + "_diagonal"] = grid_table(
            ["Dataset", "Method", "Variant"] + [name for _, name in columns], diagonal,
            context + "Each model is fine-tuned and tested on its own variant (C-a). " + notes + uncertainty,
            prefix + "-" + kind + "-diagonal")
        all_rows = [[DATASETS[dataset], method, train, test] +
                    [metric_cell(summary["cells"][train][test]["metrics"][key]) for key, _ in columns]
                    for train in variants for test in variants]
        files[kind + "_all"] = grid_table(
            ["Dataset", "Method", "Train", "Test"] + [name for _, name in columns], all_rows,
            context + f"All train-to-test combinations; {len(variants)} independently fine-tuned checkpoints. " + notes + uncertainty,
            prefix + "-" + kind + "-all")
    matrices = (("accuracy", "Accuracy"), ("macro_f1", "Macro-F1")) + ((("mrr", "MRR"),) if include_lp else ())
    for key, label in matrices:
        rows = [[train] + [metric_cell(summary["cells"][train][test]["metrics"][key]) for test in variants]
                for train in variants]
        files["transfer_" + key] = grid_table(
            [r"Train $\backslash$ Test"] + list(variants), rows,
            context + f"{label} transfer matrix. Rows identify the training graph and columns the test graph. "
            "The diagonal is matched-variant evaluation (C-a); off-diagonal cells are cross-representation transfer (C-b). "
            + uncertainty, prefix + "-transfer-" + key.replace("_", "-"))
    rows = [[method, latex_escape(pair)] + [metric_cell(result["metrics"][key]) for key, _ in PAIR_COLUMNS]
            for pair, result in sorted(summary["diagonal_pairs"].items())]
    files["per_variant_comparisons"] = grid_table(
        ["Method", "Comparison"] + [name for _, name in PAIR_COLUMNS], rows,
        context + "C-a: compare independently fine-tuned models, each tested on its own variant. "
        "Differences can reflect both training and representation. Both metrics use the original 20 candidates. "
        + uncertainty, prefix + "-per-variant-comparisons")
    transfer = []
    for train in variants:
        rows = [[method, train, latex_escape(pair)] +
                [metric_cell(result["metrics"][key]) for key, _ in PAIR_COLUMNS]
                for pair, result in sorted(summary["within_checkpoint_pairs"][train].items())]
        transfer.append(grid_table(
            ["Method", "Train", "Test comparison"] + [name for _, name in PAIR_COLUMNS], rows,
            context + f"Test-variant comparisons using the same checkpoint fine-tuned on {train}. "
            "Agreement@1 compares predictions; Kendall tau-b compares within-query rankings on the original 20 candidates. "
            + uncertainty, prefix + "-transfer-comparisons-" + train))
    files["transfer_comparisons"] = "\n".join(transfer)
    return files


def collect_runs(run_roots, include_lp):
    entries, files = {}, {}
    kinds = ("classification", "invariance") + (("link_prediction",) if include_lp else ())
    for run_root in run_roots:
        directory = run_root / "tables"
        summary = json.loads((directory / "summary.json").read_text(encoding="utf-8"))
        if summary.get("format") == "motif_finetune_matrix_v1":
            dataset, task = summary["dataset"], summary["task"]
            key = dataset, task, "finetuned_matrix"
            if key in entries:
                raise ValueError(f"Duplicate matrix run for {dataset}/{task}")
            tables = matrix_tables(summary, include_lp)
            entries[key] = {"run_root": run_root, "kinds": tuple(tables), "folder": "matrix",
                            "label": "fine-tuning matrix"}
            for kind, content in tables.items():
                files[Path("tables") / dataset / task / "matrix" / f"{kind}.tex"] = content
            continue
        for task, record in summary["tasks"].items():
            dataset = record["comparison_contract"]["dataset"]
            if dataset not in DATASETS or task not in TASKS:
                raise ValueError(f"Unsupported dataset/task: {dataset}/{task}")
            stage = record["comparison_contract"].get("evaluation_stage", "zeroshot")
            folder = ("finetuned_" + record["comparison_contract"]["fine_tuning"]["training_contract"]["train_variant"]
                      if stage == "finetuned" else "")
            key = dataset, task, folder or "zeroshot"
            if key in entries:
                raise ValueError(f"Choose one run per dataset/task/setting; duplicate {dataset}/{task}/{stage}")
            entries[key] = {"run_root": run_root, "kinds": kinds, "folder": folder,
                            "label": folder.replace("_", " ") if folder else "zero-shot"}
            for kind in kinds:
                path = Path("tables") / dataset / task / folder / f"{kind}.tex"
                text = presentation_table(record, dataset, task, kind, summary["bootstrap"])
                if folder:
                    text = text.replace(f"tab:motif-{dataset}-{task.replace('_', '-')}-",
                                        f"tab:motif-{dataset}-{task.replace('_', '-')}-{folder.replace('_', '-')}-")
                files[path] = text
    if not entries:
        raise ValueError("No task tables found")
    return entries, kinds, files


def main_document(entries, kinds):
    lines = [r"\documentclass[11pt,a4paper]{article}",
             r"\usepackage[margin=1in]{geometry}",
             r"\usepackage{adjustbox}", r"\usepackage{placeins}",
             r"\begin{document}", ""]
    first_dataset = True
    for dataset, label in DATASETS.items():
        tasks = [task for task in TASKS if any(key[:2] == (dataset, task) for key in entries)]
        if not tasks:
            continue
        if not first_dataset:
            lines.append(r"\clearpage")
        first_dataset = False
        for task in tasks:
            for key, entry in entries.items():
                if key[:2] != (dataset, task):
                    continue
                lines.append(f"\\section*{{{label}: {TASKS[task]} ({entry['label']})}}")
                for kind in entry["kinds"]:
                    path = (Path("tables") / dataset / task / entry["folder"] / f"{kind}.tex").as_posix()
                    lines.extend([f"\\input{{{path}}}", r"\FloatBarrier"])
                lines.append("")
    return "\n".join(lines + [r"\end{document}", ""])


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--run", type=Path, action="append", required=True,
                        help="Result run directory; repeat for other datasets or tasks")
    parser.add_argument("--output", type=Path, default=ROOT / "results/overleaf/motif_zeroshot_tables")
    parser.add_argument("--include-lp", action="store_true", help="Also include MRR/Hits tables")
    args = parser.parse_args()
    output = args.output.resolve()
    archive = output.parent / (output.name + ".zip")
    if output.exists() or archive.exists():
        parser.error("Output directory or ZIP already exists; choose a fresh --output")
    try:
        entries, kinds, files = collect_runs([path.resolve() for path in args.run], args.include_lp)
    except (OSError, ValueError, KeyError) as error:
        parser.error(str(error))
    files[Path("main.tex")] = main_document(entries, kinds)
    files[Path("README.md")] = (
        "# MOTIF Overleaf project\n\n"
        "Upload this ZIP as a new Overleaf project, with main.tex as the main document.\n"
        "Edit main.tex to choose which tables appear. Dataset/task folders keep filenames distinct.\n\n"
        "The presentation copies include physical variants and their pairwise comparisons only.\n"
        "They retain the numbers and uncertainty from the saved reports; no metrics were recomputed.\n\n"
        "## Source runs\n\n" + "\n".join(
            f"- {DATASETS[dataset]} / {TASKS[task].replace('--', '-')} / {entry['label']}: `{entry['run_root'].as_posix()}`"
            for (dataset, task, _), entry in entries.items()) + "\n"
    )
    output.mkdir(parents=True)
    for relative, content in files.items():
        path = output / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
    with zipfile.ZipFile(archive, "w", compression=zipfile.ZIP_DEFLATED) as stream:
        for relative in sorted(files):
            stream.write(output / relative, arcname=relative.as_posix())
    print(f"Overleaf project: {output}\nUpload ZIP: {archive}")


if __name__ == "__main__":
    main()
