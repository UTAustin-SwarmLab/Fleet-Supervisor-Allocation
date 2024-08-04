conda activate fsa
CUDA_VISIBLE_DEVICES=1 python -m main @scripts/args_ballbalance_NCUR.txt --logdir_suffix NCUR_real \
    --seed 2 --warmup_penalty 1750 --network real --allocation NCUR 
CUDA_VISIBLE_DEVICES=1 python -m main @scripts/args_ballbalance_NCUR.txt --logdir_suffix NCUR_scarce \
    --seed 2 --warmup_penalty 1750 --network scarce --allocation NCUR
CUDA_VISIBLE_DEVICES=1 python -m main @scripts/args_ballbalance_NCUR.txt --logdir_suffix NCUR_fiveg \
    --seed 2 --warmup_penalty 1750 --network fiveg --allocation NCUR

CUDA_VISIBLE_DEVICES=1 python -m main @scripts/args_ballbalance_NCUR.txt --logdir_suffix NCUR_real \
    --seed 3 --warmup_penalty 1750 --network real --allocation NCUR 
CUDA_VISIBLE_DEVICES=1 python -m main @scripts/args_ballbalance_NCUR.txt --logdir_suffix NCUR_scarce \
    --seed 3 --warmup_penalty 1750 --network scarce --allocation NCUR
CUDA_VISIBLE_DEVICES=1 python -m main @scripts/args_ballbalance_NCUR.txt --logdir_suffix NCUR_fiveg \
    --seed 3 --warmup_penalty 1750 --network fiveg --allocation NCUR