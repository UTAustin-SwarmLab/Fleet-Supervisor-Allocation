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


network_type="base"

for i in {1..3}; 
do
    
    # Runs with n-ASA allocation      
    python -m main @scripts/args_humanoid_ASA.txt --network $network_type \
    --logdir_suffix NASA --seed $i --allocation NASA

    # Runs with ASA allocation                                                                       
    python -m main @scripts/args_humanoid_ASA.txt --network $network_type \
    --logdir_suffix ASA --seed $i --allocation ASA 

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

    # Runs n-FD allocation
    python -m main @scripts/args_humanoid_NCUR.txt --logdir_suffix NCUR \
    --seed $i --network $network_type --allocation NCUR \
    --connection_thresh 0.4

done