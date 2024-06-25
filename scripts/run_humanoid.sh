# Description: Runs all allocation policies for Humanoid, for 3 seeds each.
# Change network type to be ["scarce", "fiveg", "scarce", "real"] for 
# different network types.
    # scarce --> "Always"
    # fiveg --> "5G Network"
    # scarce --> "Mixed-Scarce"
    # real --> "Ookla"

# Allocation types are ["NASM", "ASM", "CUR", "random", "UC"]
    # NASM --> "n-ASA"
    # ASM --> "ASA"
    # CUR --> "FD"
    # random --> "Random"
    # allocation CUR, order UC --> "FE"


network_type="base"

for i in {1..3}; 
do
    
    # Runs with n-ASA allocation      
    python -m main @scripts/args_humanoid_ASM.txt --network $network_type \
    --logdir_suffix NASM --seed $i --allocation NASM

    # Runs with ASA allocation                                                                       
    python -m main @scripts/args_humanoid_ASM.txt --network $network_type \
    --logdir_suffix ASM --seed $i --allocation ASM 

    # Runs with FD allocation      
    python -m main @scripts/args_humanoid.txt --logdir_suffix CUR \
    --seed $i --warmup_penalty 1000 --network $network_type --allocation CUR 

    # Runs with Random allocation      
    python -m main @scripts/args_humanoid.txt --logdir_suffix Random \
    --allocation random --seed $i --std_dev 0.05 --action_budget 20000 \
    --network $network_type

    # Runs with FE allocation      
    python -m main @scripts/args_humanoid.txt --logdir_suffix Ensemble \
    --seed $i --order UC --network $network_type

done