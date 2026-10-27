# MOTIF guide-based Overleaf project

Upload the ZIP and compile main.tex on Overleaf.
For an existing project, replace main.tex and upload tables/ with the same hierarchy.
Old classification and duplicate fine-tuning table files may be deleted from Overleaf.

IMDb uses the correct target plus 19 fixed negative targets; DBLP ranks all 20 conferences.
Zero-shot has one MRR/Hits table and one Agreement/Kendall tau/Delta MRR table per task.

## Source runs

- `results/motif_zeroshot_imdb_lp_full`
- `results/motif_zeroshot_dblp_lp_full`
