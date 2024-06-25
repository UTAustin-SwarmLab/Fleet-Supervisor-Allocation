# Description: Runs all allocation policies for Ball Balance, for 3 seeds each.
# Change network type to be ["base", "fiveg", "scarce", "real"] for 
# different network types.
    # base --> "Always"
    # fiveg --> "5G Network"
    # scarce --> "Mixed-Scarce"
    # real --> "Ookla"

# Allocation types are ["NASM", "ASM", "CUR", "random", "UC"]
    # NASM --> "n-ASA"
    # ASM --> "ASA"
    # CUR --> "FD"
    # random --> "Random"
    # allocation CUR, order UC --> "FE"
    # TD --> "FD"

network_type="base"

for i in {1..3}; 
do

    # Runs with n-ASA allocation                                                                                                         
    python -m main @scripts/args_ballbalance_ASM.txt --network $network_type \
    --logdir_suffix NASM --seed $i --allocation NASM 

    # Runs with ASA allocation                                                                       
    python -m main @scripts/args_ballbalance_ASM.txt --network $network_type \
    --logdir_suffix ASM --seed $i --allocation ASM 

    # Runs with FD allocation                                                                       
    python -m main @scripts/args_ballbalance.txt --logdir_suffix CUR \
    --seed $i --warmup_penalty 1750 --network $network_type --allocation CUR 

    # Runs with Random allocation                                                                       
    python -m main @scripts/args_ballbalance.txt --logdir_suffix Random \
    --seed $i --std_dev 0.05 --action_budget 50000 --allocation random \
    --network $network_type

    # Runs with FE allocation                                                                       
    python -m main @scripts/args_ballbalance.txt --logdir_suffix Ensemble \
    --seed $i --order UC --network $network_type --allocation CUR

    # Runs with FT allocation                                                                       
    python -m main @scripts/args_ballbalance.txt --logdir_suffix TD \
    --seed $i --alpha_weight 0.5 --combined_alpha_thresh 0.15 --goal_critic \
    --no_safety_critic --allocation TD --network $network_type

done