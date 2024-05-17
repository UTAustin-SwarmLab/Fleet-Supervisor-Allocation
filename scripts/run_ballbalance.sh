for i in {1..3}; do
    python -m main @scripts/args_ballbalance.txt --env_name ballbalance --risk_thresh 0.19805172376011418 --uncertainty_thresh 0.1830047384932709 --marginal_increase_threshold 0.2297221043672124 --similarity_alpha 28.028502675363985 --state_similarity_ratio 0.49862689004367816 --uncertainty_ratio 0.10302943197858241 --warmup_penalty 2500 --network base --logdir_suffix NASM --seed 1 --allocation NASM &

    python -m main @scripts/args_ballbalance.txt --env_name ballbalance  --logdir_suffix F.D. --seed $i --warmup_penalty 1000 --network base --allocation CUR &

    python -m main @scripts/args_ballbalance.txt --env_name ballbalance --logdir_suffix Random --allocation random --seed $i --std_dev 0.05 --action_budget 1000 &

    python -m main @scripts/args_ballbalance.txt --env_name ballbalanceß  --logdir_suffix F.E. --seed $i --order UC --network base
done
ƒ