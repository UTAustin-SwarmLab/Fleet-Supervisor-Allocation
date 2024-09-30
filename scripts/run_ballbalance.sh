# Description: Runs all allocation policies for Allegro Hand, for 3 seeds each.
# Change network type to be ["always", "fiveg", "scarce", "real"] for 
# different network types.
    # always --> "Always"
    # fiveg --> "5G Network"
    # mixed-scarce --> "Mixed-Scarce"
    # ookla --> "Ookla"
    # changing-scarce --> "Changing-Scarce"

# Allocation types are ["NASA", "ASA", "CUR", "random", "UC", "NCUR"]
    # NASA --> "n-ASA"
    # ASA --> "ASA"
    # CUR --> "FD"
    # random --> "Random"
    # allocation CUR, order UC, Ensemble --> "FE"
    # NCUR --> "n-FD"
    # CUR --> "FD"
    # TD --> "FT"

seeds=(1000 2000 3000)
network_type="base"

for i in "${seeds[@]}"
do

    # Runs with n-ASA allocation                                                                                                         
    python -m main @scripts/args_ballbalance_ASA.txt --network $network_type \
    --logdir_suffix NASA --seed $i --allocation NASA 

    # Runs with ASA allocation                                                                       
    python -m main @scripts/args_ballbalance_ASA.txt --network $network_type \
    --logdir_suffix ASA --seed $i --allocation ASA 

    # Runs with FD allocation                                                                       
    python -m main @scripts/args_ballbalance.txt --logdir_suffix CUR \
    --seed $i --warmup_penalty 1750 --network $network_type --allocation CUR 

    # Runs with Random allocation                                                                       
    python -m main @scripts/args_ballbalance.txt --logdir_suffix Random \
    --seed $i --std_dev 0.05 --action_budget 50000 --allocation random \
    --network $network_type

    # Runs with FE allocation                                                                       
    python -m main @scripts/args_ballbalance.txt --logdir_suffix Ensemble \
    --seed $i --order UC --network $network_type --allocation CUR \
    --uncertainty_thresh 0.375

    # Runs with FT allocation                                                                       
    python -m main @scripts/args_ballbalance.txt --logdir_suffix TD \
    --seed $i --alpha_weight 0.5 --combined_alpha_thresh 0.15 --goal_critic \
    --no_safety_critic --allocation TD --network $network_type

    # Runs n-FD allocation
    python -m main @scripts/args_ballbalance_NCUR.txt --logdir_suffix NCUR \
    --seed $i --network $network_type --allocation NCUR \
    --connection_thresh 0.4

done