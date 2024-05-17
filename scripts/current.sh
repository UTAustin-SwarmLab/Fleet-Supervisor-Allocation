conda activate fleet_super
for i in {1..3};
do

python -m main @scripts/args_humanoid_NASM.txt --env_name Humanoid --warmup_penalty 2500 --network scarce --logdir_suffix ASM_scarce --seed 1 --allocation ASM &

python -m main @scripts/args_humanoid_NASM.txt --env_name Humanoid --warmup_penalty 2500 --network scarce --logdir_suffix NASM_scarce --seed 1 --allocation NASM &

python -m main @scripts/args_humanoid.txt --env_name Humanoid  --logdir_suffix CUR_scarce --seed 1 --warmup_penalty 1000 --network scarce --allocation CUR 

done