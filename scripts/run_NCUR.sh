conda activate fsa
CUDA_VISIBLE_DEVICES=1 python -m main @scripts/args_allegro_NCUR.txt --logdir_suffix NCUR_0.4_real \
    --seed 1 --warmup_penalty 2500 --network real --allocation NCUR --connection_thresh 0.4 \
    --logdir /home/ugrad-su24/ege/Fleet-Supervisor-Allocation/logs/allegro_real

CUDA_VISIBLE_DEVICES=2 python -m main @scripts/args_allegro_NCUR.txt --logdir_suffix NCUR_0.4_fiveg \
    --seed 1 --warmup_penalty 2500 --network fiveg --allocation NCUR --connection_thresh 0.4 \
    --logdir /home/ugrad-su24/ege/Fleet-Supervisor-Allocation/logs/allegro_fiveg


CUDA_VISIBLE_DEVICES=2 python -m main @scripts/args_allegro_NCUR.txt --logdir_suffix NCUR_0.4_real \
    --seed 2 --warmup_penalty 2500 --network real --allocation NCUR --connection_thresh 0.4 \
    --logdir /home/ugrad-su24/ege/Fleet-Supervisor-Allocation/logs/allegro_real

CUDA_VISIBLE_DEVICES=5 python -m main @scripts/args_allegro_NCUR.txt --logdir_suffix NCUR_0.4_fiveg \
    --seed 2 --warmup_penalty 2500 --network fiveg --allocation NCUR --connection_thresh 0.4 \
    --logdir /home/ugrad-su24/ege/Fleet-Supervisor-Allocation/logs/allegro_fiveg


CUDA_VISIBLE_DEVICES=1 python -m main @scripts/args_allegro_NCUR.txt --logdir_suffix NCUR_0.4_real \
    --seed 3 --warmup_penalty 2500 --network real --allocation NCUR --connectivity_thresh 0.4 \
    --logdir /home/ugrad-su24/ege/Fleet-Supervisor-Allocation/logs/allegro_real

CUDA_VISIBLE_DEVICES=6 python -m main @scripts/args_allegro_NCUR.txt --logdir_suffix NCUR_0.4_fiveg \
    --seed 3 --warmup_penalty 2500 --network fiveg --allocation NCUR --connectivity_thresh 0.4 \
    --logdir /home/ugrad-su24/ege/Fleet-Supervisor-Allocation/logs/allegro_fiveg