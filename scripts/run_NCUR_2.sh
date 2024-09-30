conda activate fsa
CUDA_VISIBLE_DEVICES=5 python -m main @scripts/args_anymal_NCUR.txt --logdir_suffix NCUR_0.4_n \
    --seed 2 --network changing --allocation NCUR \
    --logdir /nas/oguzhan/fleet_supervision/rebuttal_logs/changing_network/anymal \
    --connection_thresh 0.4 &


CUDA_VISIBLE_DEVICES=6 python -m main @scripts/args_allegro_NCUR.txt --logdir_suffix NCUR_0.4_n \
    --seed 2 --network changing --allocation NCUR \
    --logdir /nas/oguzhan/fleet_supervision/rebuttal_logs/changing_network/allegro \
    --warmup_penalty 500 \
    --connection_thresh 0.4 &

CUDA_VISIBLE_DEVICES=7 python -m main @scripts/args_ballbalance_NCUR.txt --logdir_suffix NCUR_0.4_n \
    --seed 2 --network changing --allocation NCUR \
    --logdir /nas/oguzhan/fleet_supervision/rebuttal_logs/changing_network/ballbalance \
    --connection_thresh 0.4 &

CUDA_VISIBLE_DEVICES=3 python -m main @scripts/args_humanoid_NCUR.txt --logdir_suffix NCUR_0.4_n \
    --seed 2 --network changing --allocation NCUR \
    --logdir /nas/oguzhan/fleet_supervision/rebuttal_logs/changing_network/humanoid \
    --connection_thresh 0.4 &