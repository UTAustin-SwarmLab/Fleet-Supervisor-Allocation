conda activate fsa
CUDA_VISIBLE_DEVICES=2 python -m main @scripts/args_allegro_NCUR.txt --logdir_suffix NCUR_0.6_real \
    --seed 1 --warmup_penalty 2500 --network real --allocation NCUR --connection_thresh 0.6
CUDA_VISIBLE_DEVICES=2 python -m main @scripts/args_allegro_NCUR.txt --logdir_suffix NCUR_0.6_scarce \
    --seed 1 --warmup_penalty 2500 --network scarce --allocation NCUR --connection_thresh 0.6
CUDA_VISIBLE_DEVICES=2 python -m main @scripts/args_allegro_NCUR.txt --logdir_suffix NCUR_0.6_fiveg \
    --seed 1 --warmup_penalty 2500 --network fiveg --allocation NCUR --connection_thresh 0.6

CUDA_VISIBLE_DEVICES=2 python -m main @scripts/args_allegro_NCUR.txt --logdir_suffix NCUR_0.6_real \
    --seed 2 --warmup_penalty 2500 --network real --allocation NCUR --connection_thresh 0.6
CUDA_VISIBLE_DEVICES=2 python -m main @scripts/args_allegro_NCUR.txt --logdir_suffix NCUR_0.6_scarce \
    --seed 2 --warmup_penalty 2500 --network scarce --allocation NCUR --connection_thresh 0.6
CUDA_VISIBLE_DEVICES=2 python -m main @scripts/args_allegro_NCUR.txt --logdir_suffix NCUR_0.6_fiveg \
    --seed 2 --warmup_penalty 2500 --network fiveg --allocation NCUR --connection_thresh 0.6

CUDA_VISIBLE_DEVICES=2 python -m main @scripts/args_allegro_NCUR.txt --logdir_suffix NCUR_0.6_real \
    --seed 3 --warmup_penalty 2500 --network real --allocation NCUR --connectivity_thresh 0.6
CUDA_VISIBLE_DEVICES=2 python -m main @scripts/args_allegro_NCUR.txt --logdir_suffix NCUR_0.6_scarce \
    --seed 3 --warmup_penalty 2500 --network scarce --allocation NCUR --connectivity_thresh 0.6
CUDA_VISIBLE_DEVICES=2 python -m main @scripts/args_allegro_NCUR.txt --logdir_suffix NCUR_0.6_fiveg \
    --seed 3 --warmup_penalty 2500 --network fiveg --allocation NCUR --connectivity_thresh 0.6