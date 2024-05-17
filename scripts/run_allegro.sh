for i in {1..3}; do
    python -m main @scripts/args_allegro.txt --env_name AllegroHand --risk_thresh 0.1237800553492419 --uncertainty_thresh 0.20064363566533475 --marginal_increase_threshold 0.03877548214572482 --similarity_alpha 16.143536420083507 --state_similarity_ratio 0.36725692057550907 --uncertainty_ratio 0.526482643854261 --warmup_penalty 1250 --network base --logdir_suffix NASM --seed $i --allocation NASM &

    python -m main @scripts/args_allegro.txt --env_name AllegroHand  --logdir_suffix F.D. --seed $i --warmup_penalty 1000 --network base --allocation CUR &

    python -m main @scripts/args_allegro.txt --env_name Allegro Hand --logdir_suffix Random --allocation random --seed $i --std_dev 0.05 --action_budget 3000 &

    python -m main @scripts/args_allegro.txt --env_name AllegroHand  --logdir_suffix F.E. --seed $i --order UC --network base
done