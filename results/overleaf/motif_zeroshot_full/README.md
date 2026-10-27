# MOTIF guide-based Overleaf project

Upload the ZIP and compile main.tex on Overleaf.
For an existing project, replace main.tex and upload tables/ with the same hierarchy.
Old classification and duplicate fine-tuning table files may be deleted from Overleaf.

IMDb uses the correct target plus 19 fixed negative targets; DBLP ranks all 20 conferences.
Zero-shot has one MRR/Hits table and one Agreement/Kendall tau/Delta MRR table per task.
DBLP zero-shot adds a macro Precision/Recall/F1 table; Accuracy and Micro-F1 are omitted because they equal Hits@1.

## IMDb fine-tuning: exactly two tables

- `tables/imdb/movie_year/matrix/transfer_performance.tex`: 16 rows with Fine-tuned on, Test graph, MRR and Hits@1/3/10 columns.
- `tables/imdb/movie_year/matrix/invariance.tex`: six C-a pairs of independently trained diagonal models, plus 24 C-b test-variant pairs grouped by fixed checkpoint.
- `training_notes.tex` supplies prose method/cost notes, not another table.

Matching Fine-tuned on/Test graph labels are matched-variant evaluation (C-a); the other 12 rows are transfer (C-b).
Each performance row evaluates one checkpoint on one graph. Each invariance row compares two such outputs.
Delta MRR is the second test variant minus the first. All metrics use the same 20 candidates.
C-a changes both weights and graphs; each C-b group holds weights fixed.
Single training seed 1024; uncertainty is query-bootstrap SE. The guide's repeated-training floor
and across-training-seed mean/SD are not yet measured.

## Source runs

- `results/motif_zeroshot_imdb_lp_full`
- `results/motif_zeroshot_dblp_lp_full`
- `results/motif_finetune_matrix_imdb_lp_matrix_s1024`
