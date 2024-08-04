conda activate fsa
gpu=7
network=fiveg

for i in {0..20}; do
CUDA_VISIBLE_DEVICES=$gpu python -m optuna_optimize_anymal_fiveg @scripts/args_anymal.txt \
    --warmup_penalty 250 \
    --allocation CUR \
    --seed 0 \
    --network $network \
    --logdir /nas/oguzhan/fleet_supervision/rebuttal_logs/${network}
done