# Combine IMDb and DBLP tables in Overleaf

The presentation project uses simple bordered tables: Dataset, Method, Variant,
Accuracy, Precision, Recall, Micro-F1 and Macro-F1; then a separate Method,
Comparison, Agreement@1 and Kendall tau-b table. Dataset/task folders keep filenames distinct.
It uses previously generated reports and does not rerun inference, recompute
metrics, load score arrays or compile a PDF locally.

After generating reports on the HPC and pulling them locally, run from MOTIF:

```bash
python script/export_overleaf.py \
  --run results/motif_zeroshot_imdb_lp_full \
  --run results/motif_zeroshot_dblp_lp_full \
  --output results/overleaf/motif_zeroshot_tables
```

This needs only Python's standard library, so it also works on the HPC or in a
local Python environment without Torch. Choose a fresh `--output` when making a
new version. Add `--include-lp` to include MRR/Hits tables. To add Movie-Director
later, supply its completed result directory as another `--run`; use only one
run per dataset/task/evaluation setting.

The project layout is:

```text
results/overleaf/
  motif_zeroshot_tables.zip
  motif_zeroshot_tables/
    main.tex
    README.md
    tables/
      imdb/
        movie_year/
          classification.tex
          invariance.tex
      dblp/
        paper_conference/
          classification.tex
          invariance.tex
```

Upload `motif_zeroshot_tables.zip` as a new Overleaf project. Set `main.tex` as the
main document if necessary, then Recompile and download the PDF. In an existing
project, retain the folder hierarchy and copy the corresponding `\input` paths
from `main.tex`. Edit those lines to choose which tables appear. The template
groups tasks by dataset and includes table-width limits to fit the page.

## Include the IMDb fine-tuning matrix

After the four fine-tunes and 16 evaluations have generated their combined report,
add that matrix directory as another source. Zero-shot and fine-tuned Movie-Year
results can share the same project:

```bash
python script/export_overleaf.py \
  --run results/motif_zeroshot_imdb_lp_full \
  --run results/motif_zeroshot_dblp_lp_full \
  --run results/motif_finetune_matrix_imdb_lp_matrix_s1024 \
  --output results/overleaf/motif_zero_and_finetuned_s1024
```

The matrix uses `tables/imdb/movie_year/matrix/` and distinct LaTeX labels. It
contains the four matched-variant results, all 16 Train/Test rows, Accuracy and
Macro-F1 transfer matrices, and Agreement@1/Kendall tau-b comparisons. Comparisons
between independently trained models and comparisons using one fixed checkpoint
are separate tables with explicit captions. Add `--include-lp` for the separate
MRR/Hits tables and MRR matrix.

Edit the `\input` lines in the exported `main.tex` to select tables. For example,
retain `matrix/classification_all.tex` and `matrix/transfer_comparisons.tex` for
the full classification results and the four sets of fixed-checkpoint ranking
comparisons. All uncertainty in this single-seed experiment is query-bootstrap
SE, not standard deviation across training seeds.

The exporter needs only `tables/summary.json` from each source run. Large score
arrays and training checkpoints can stay on the HPC. See the
[fine-tuning runbook](IMDB_FINE_TUNING.md) for training and report commands.

## What “compiled” meant in the source reports

The source `compiled` view is SCR's existing semantic-program graph, exported
from the canonical preprocessing bundles. Each variant maps to the same graph
within a task. MOTIF receives that graph as input, so identical inputs can
produce identical results. This does not implement or demonstrate a learned
invariance algorithm inside MOTIF. It is also separate from MOTIF's Lift,
which constructs a relation hypergraph for each input graph.

The presentation copies show only the physical graph variants whose outputs
we are comparing. Original report files and saved numerical results are retained.
Only labels, layout, selection of rows/tables and presentation wording change.
