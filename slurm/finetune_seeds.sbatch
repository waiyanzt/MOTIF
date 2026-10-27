#!/bin/bash
# Fine-tuning matrix for the lab's three training seeds, one array task per seed.
#   sbatch slurm/finetune_seeds.sbatch                      # IMDb movie_year
#   sbatch --export=ALL,DATASET=dblp slurm/finetune_seeds.sbatch
#   sbatch -p dgx2 --constraint=v100 slurm/finetune_seeds.sbatch   # any GPU; arch is detected below
# Keep all seeds of one table on the same GPU type (the CMPNN baselines ran on V100).
# Then build the seed-averaged tables with script/report_seeds.py (see docs/SEED_TABLES.md).
#SBATCH -J motif-ft-seeds
#SBATCH -A eecs
#SBATCH -p dgxh
#SBATCH --gres=gpu:1
#SBATCH -c 8
#SBATCH --mem=32G
#SBATCH -t 1-00:00:00
#SBATCH --array=0-2
#SBATCH -o logs/%x-%A_%a.out
#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user=tinw@oregonstate.edu

set -euo pipefail
SEEDS=(1566911444 20241017 20251017)  # SCR METRICS.md seeds, shared with the CMPNN results
SEED=${SEEDS[$SLURM_ARRAY_TASK_ID]}
DATASET=${DATASET:-imdb}
RUN_TAG=${RUN_TAG:-seeds}

module load python/3.10 gcc/12.2 cuda/12.1
cd "$SLURM_SUBMIT_DIR"
source .venv/bin/activate

export CC="$(command -v gcc)" CXX="$(command -v g++)"
# One extension cache per GPU architecture (7.0 V100, 7.5 RTX 2080/8000, 8.6 A40, 9.0 H100/H200).
ARCH=$(nvidia-smi --query-gpu=compute_cap --format=csv,noheader | head -1)
export TORCH_CUDA_ARCH_LIST="$ARCH"
export TORCH_EXTENSIONS_DIR="$PWD/.cache/torch_extensions_cu121_sm${ARCH/./}"
export TRITON_CACHE_DIR="$PWD/.cache/triton"
export MAX_JOBS=4 PYTHONHASHSEED=0 CUBLAS_WORKSPACE_CONFIG=:4096:8 PYTHONUNBUFFERED=1

echo "host=$(hostname) dataset=$DATASET seed=$SEED tag=$RUN_TAG commit=$(git rev-parse --short HEAD)"
nvidia-smi --query-gpu=name,memory.total --format=csv,noheader

if [[ ${SMOKE:-0} == 1 ]]; then  # Two updates on v1: checks the training path before the full array.
  python -u script/finetune_${DATASET}_lp.py --train-variant v1 --seed "$SEED" \
    --steps 2 --validate-every 2 --val-limit 16 --run-tag "smoke_${SLURM_JOB_ID}"
  exit
fi

python -u script/run_finetune_matrix.py \
  --dataset "$DATASET" --seed "$SEED" --run-tag "$RUN_TAG" \
  --steps 1000 --validate-every 100 --resume
