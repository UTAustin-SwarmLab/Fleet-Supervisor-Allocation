# Description: Runs all allocation policies for Anymal, for 3 seeds each.
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


network_type="fiveg"

for i in {1..3}; 
do
    # Runs with n-ASA allocation                                                                         
    python -m main @scripts/args_anymal_ASM.txt --network $network_type \
    --logdir_suffix NASM --seed $i --allocation NASM 

    # Runs with ASA allocation      
    python -m main @scripts/args_anymal_ASM.txt --network $network_type \
    --logdir_suffix ASM --seed $i --allocation ASM 
 
    # Runs with FD allocation      
    python -m main @scripts/args_anymal.txt --logdir_suffix CUR \
    --seed $i --warmup_penalty 250 --network $network_type --allocation CUR 

    # Runs with Random allocation      
    python -m main @scripts/args_anymal.txt --logdir_suffix Random \
    --seed $i --std_dev 0.05 --action_budget 4000 --allocation random \
    --network $network_type

    # Runs with FE allocation      
    python -m main @scripts/args_anymal.txt --logdir_suffix Ensemble \
    --seed $i --order UC --network $network_type --allocation CUR

done