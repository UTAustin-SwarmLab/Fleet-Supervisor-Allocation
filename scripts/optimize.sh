conda activate fsa
gpu=4
network=scarce

for i in {0..20}; do
CUDA_VISIBLE_DEVICES=$gpu python -m optuna_optimize_humanoid_scarce @scripts/args_humanoid.txt \
    --warmup_penalty 1000 \
    --allocation CUR \
    --seed 0 \
    --network $network \
    --logdir /nas/oguzhan/fleet_supervision/rebuttal_logs/${network}
done