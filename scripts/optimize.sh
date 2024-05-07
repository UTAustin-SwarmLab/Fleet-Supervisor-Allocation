conda activate fleet_super
for i in {1..10}; do
CUDA_VISIBLE_DEVICES=5 python -m optuna_optimize_6 @scripts/args_humanoid_2.txt --logdir_suffix humanoid_opt_base_NASM --allocation NASM --seed 1 --network base --warmup_penalty 1000
done


