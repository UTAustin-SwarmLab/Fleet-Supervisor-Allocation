network_type=scarce

python -m main @scripts/args_humanoid_NCUR.txt --logdir_suffix NCUR \
    --seed 0 --warmup_penalty 1000 --network $network_type --allocation NCUR 