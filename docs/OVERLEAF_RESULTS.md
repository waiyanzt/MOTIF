# MOTIF results in Overleaf

The presentation follows the candidate protocol in guide B2: IMDb Movie-Year
ranks the correct year against the same 19 fixed negative years; DBLP ranks all
20 conferences. All presentation metrics use those candidates.

The combined project is `results/overleaf/motif_zeroshot_full/`; the name is
retained for continuity. Its ZIP contains IMDb and DBLP zero-shot results and the
IMDb fine-tuning results.

## Tables

Each zero-shot dataset/task has two tables:

* `link_prediction.tex`: MRR and Hits@1/3/10 per physical variant.
* `invariance.tex`: Agreement@1, Kendall tau-b and Delta MRR for variant pairs,
  with the released checkpoint fixed.

DBLP zero-shot also has `conference_prediction.tex` with macro Precision, Recall
and F1. Accuracy and Micro-F1 are omitted because they equal Hits@1 there.

IMDb Movie-Year fine-tuning has exactly two tables in
`tables/imdb/movie_year/matrix/`:

* `transfer_performance.tex`: 16 rows with Fine-tuned on, Test graph, MRR and
  Hits@1/3/10 columns. Matching train/test variants are matched-variant evaluation
  (C-a); the other 12 rows are cross-representation transfer (C-b).
* `invariance.tex`: Agreement@1, Kendall tau-b and Delta MRR, with Regime,
  Checkpoint trained on and Test graphs compared labels. C-a compares the separately trained diagonal models; C-b compares test
  variants with each selected checkpoint fixed, including its matched reference.
  There are six C-a comparisons plus 24 C-b comparisons. Each row compares two
  prediction outputs; a single train/test performance row supplies one output.

DBLP Paper-Conference fine-tuning has at most three tables in
`tables/dblp/paper_conference/matrix/`:

* `conference_prediction.tex`: macro Precision, Recall and F1 (Accuracy and Micro-F1 equal Hits@1).
* `link_prediction.tex`: MRR and Hits@1/3/10 for the same train/test cells.
* `invariance.tex`: C-a/C-b labelled Agreement@1, Kendall tau-b and Delta MRR.

Both DBLP performance tables combine all nine Train/Test cells: matching labels
are C-a and different labels are C-b. All metrics use the same 20 conferences;
there is no extra node-classification experiment. See the
[DBLP fine-tuning runbook](DBLP_FINE_TUNING.md).

Delta MRR is always the second test variant minus the first. The extra full-year
prediction tables and duplicate diagonal/all-cell tables are removed from the
presentation. Recorded training cost and target-edge removal counts appear as
method notes rather than additional tables.

This is a single-training-seed preliminary experiment. Error bars are
query-bootstrap SE, not the across-training-seed mean/SD requested for the full
guide protocol. Repeated training and the multi-seed noise floor remain pending.

## Upload the existing project

Upload `results/overleaf/motif_zeroshot_full.zip` as a new Overleaf project and
compile `main.tex`. To update an existing Overleaf project, replace `main.tex`
and upload the updated `tables/` contents while retaining the folder hierarchy.
The previous classification files can be deleted from the Overleaf project;
the new main document does not reference them. No local PDF compilation is needed.

## Generate a new export from saved reports

Run from MOTIF, on the HPC or locally after pulling the text reports:

```bash
python script/export_overleaf.py \
  --run results/motif_zeroshot_imdb_lp_full \
  --run results/motif_zeroshot_dblp_lp_full \
  --run results/motif_finetune_matrix_imdb_lp_matrix_s1024 \
  --output results/overleaf/motif_guide_results
```

Choose a fresh `--output` for later exports. LP is included by default; the old
`--include-lp` flag is accepted for compatibility. The exporter uses only
Python's standard library and saved summaries. If older matrix summaries lack
cost fields, it also reads the corresponding saved training summaries when
available. It does not load model checkpoints or raw score arrays.

Dataset/task folders and distinct LaTeX labels keep zero-shot and fine-tuned
results separate in one document. Edit `main.tex` to choose which tables appear.
See the [fine-tuning runbook](IMDB_FINE_TUNING.md) for the experiment commands.

## Source records

Original numerical summaries, score files and checkpoint provenance remain
unchanged. Historical extra metrics may still be present in numerical records;
they are not included in the guide-based presentation. Compiled and repeat
controls are also kept outside the presentation.
