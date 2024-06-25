
network_type="fiveg"

    # Runs with n-ASA allocation                                                                                                         
    python -m main @scripts/args_ballbalance_ASM.txt --network $network_type \
    --logdir_suffix NASM_fiveg --seed $i --allocation NASM 

    # Runs with ASA allocation                                                                       
    python -m main @scripts/args_ballbalance_ASM.txt --network $network_type \
    --logdir_suffix ASM_fiveg --seed $i --allocation ASM 

    # Runs with FD allocation                                                                       
    python -m main @scripts/args_ballbalance.txt --logdir_suffix CUR_fiveg \
    --seed $i --warmup_penalty 1750 --network $network_type --allocation CUR 

    # Runs with Random allocation                                                                       
    python -m main @scripts/args_ballbalance.txt --logdir_suffix Random_fiveg \
    --seed $i --std_dev 0.05 --action_budget 50000 --allocation random \
    --network $network_type

    # Runs with FE allocation                                                                       
    python -m main @scripts/args_ballbalance.txt --logdir_suffix Ensemble_fiveg \
    --seed $i --order UC --network $network_type --allocation CUR

    # Runs with FT allocation                                                                       
    python -m main @scripts/args_ballbalance.txt --logdir_suffix TD_fiveg \
    --seed $i --alpha_weight 0.5 --combined_alpha_thresh 0.15 --goal_critic \
    --no_safety_critic --allocation TD --network $network_type

