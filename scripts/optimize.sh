conda activate fsa
gpu=1
network=scarce

for i in {0..10}; do
CUDA_VISIBLE_DEVICES=$gpu python -m optuna_optimize_anymal_scarce @scripts/args_anymal.txt \
    --warmup_penalty 250 \
    --allocation CUR \
    --seed 0 \
    --network $network \
    --logdir /nas/oguzhan/fleet_supervision/rebuttal_logs/${network}
done