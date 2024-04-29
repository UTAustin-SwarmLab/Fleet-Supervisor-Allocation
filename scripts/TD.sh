for i in {1..3}
do
	python -m main @scripts/args_allegro.txt --logdir_suffix allegro_real_TD --seed $i --allocation TD --alpha_weight 0.25 --combined_alpha_thresh 3.25 --goal_critic --no_safety_critic --network real
done

for i in {1..3}
do
	python -m main @scripts/args_allegro.txt --logdir_suffix allegro_base_TD --seed $i --allocation TD --alpha_weight 0.25 --combined_alpha_thresh 3.25 --goal_critic --no_safety_critic --network base
done

for i in {1..3}
do
	python -m main @scripts/args_allegro.txt --logdir_suffix allegro_drch_TD --seed $i --allocation TD --alpha_weight 0.25 --combined_alpha_thresh 3.25 --goal_critic --no_safety_critic --network drch
done