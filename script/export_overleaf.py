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


def collect_runs(run_roots, include_lp):
    entries, files = {}, {}
    kinds = ("classification", "invariance") + (("link_prediction",) if include_lp else ())
    for run_root in run_roots:
        directory = run_root / "tables"
        summary = json.loads((directory / "summary.json").read_text(encoding="utf-8"))
        for task, record in summary["tasks"].items():
            dataset = record["comparison_contract"]["dataset"]
            if dataset not in DATASETS or task not in TASKS:
                raise ValueError(f"Unsupported dataset/task: {dataset}/{task}")
            key = dataset, task
            if key in entries:
                raise ValueError(f"Choose one run per dataset/task; duplicate {dataset}/{task}")
            entries[key] = run_root
            for kind in kinds:
                path = Path("tables") / dataset / task / f"{kind}.tex"
                files[path] = presentation_table(record, dataset, task, kind, summary["bootstrap"])
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
        tasks = [task for task in TASKS if (dataset, task) in entries]
        if not tasks:
            continue
        if not first_dataset:
            lines.append(r"\clearpage")
        first_dataset = False
        for task in tasks:
            lines.append(f"\\section*{{{label}: {TASKS[task]}}}")
            for kind in kinds:
                lines.append(f"\\input{{tables/{dataset}/{task}/{kind}.tex}}")
            lines.extend([r"\FloatBarrier", ""])
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
            f"- {DATASETS[dataset]} / {TASKS[task].replace('--', '-')}: `{path.as_posix()}`"
            for (dataset, task), path in entries.items()) + "\n"
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
