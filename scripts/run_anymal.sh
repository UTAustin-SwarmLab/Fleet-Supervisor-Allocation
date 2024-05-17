
for i in {1..3}; do
    python -m main @scripts/args_anymal.txt --env_name Anymal --risk_thresh 0.49668746821959014 --uncertainty_thresh 0.19341546210164895 --critic_safe_pretraining_steps 500 --marginal_increase_threshold 0.694254883935102 --similarity_alpha 1.6398343931530426 --state_similarity_ratio 1.7252904278299146 --uncertainty_ratio 0.055490632202624054 --warmup_penalty 1000 --network base --logdir_suffix NASM --seed $i --allocation NASM &

    python -m main @scripts/args_anymal.txt --env_name Anymal  --logdir_suffix F.D. --seed $i --warmup_penalty 1000 --network base --allocation CUR &

    python -m main @scripts/args_anymal.txt --env_name Anymal --logdir_suffix Random --allocation random --seed $i --std_dev 0.05 --action_budget 100 &

    python -m main @scripts/args_anymal.txt --env_name Anymal  --logdir_suffix F.E. --seed $i --order UC --network base
done