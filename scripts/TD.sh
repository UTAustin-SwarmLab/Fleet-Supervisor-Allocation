for i in {1..3}
do
	python -m main @scripts/args_anymal.txt --logdir_suffix TD --seed $i --allocation TD --alpha_weight 0.25 --combined_alpha_thresh 3.25 --goal_critic --no_safety_critic
done