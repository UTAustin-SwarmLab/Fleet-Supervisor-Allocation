CUDA_VISIBLE_DEVICES=1 python -m main @scripts/args_anymal_NCUR.txt --logdir_suffix NCUR \
    --seed 0 --warmup_penalty 250 --network real --allocation NCUR 
CUDA_VISIBLE_DEVICES=2 python -m main @scripts/args_anymal_NCUR.txt --logdir_suffix NCUR \
    --seed 0 --warmup_penalty 250 --network scarce --allocation NCUR 
CUDA_VISIBLE_DEVICES=3 python -m main @scripts/args_anymal_NCUR.txt --logdir_suffix NCUR \
    --seed 0 --warmup_penalty 250 --network fiveg --allocation NCUR 