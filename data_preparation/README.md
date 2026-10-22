# Source provenance

`inv_gnn/` contains the small dependency closure of the original IMDb and DBLP
dataset builders used by SCR. These files are copied verbatim from
`SCR/INV-GNN-12D9/`, with their relative paths preserved so imports and pickle
class identities work unchanged. `PROVENANCE.json` records the original SHA-256
of every copied file, plus the SCR exporters/helpers from which the MOTIF entry
points were adapted.

`common/inv_rgcn/model.py` is included because the original package initializer
imports its classes. The preprocessing commands do not instantiate or train
those models. No raw datasets or model checkpoints are bundled here.

See [data preparation](../docs/DATA_PREPARATION.md) for the runnable commands and
the model-specific changes to the portable export.
