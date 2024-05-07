for i in {1..3}
do
	python -m main @scripts/args_humanoid.txt --logdir_suffix Ensemble --seed $i --order UC --network base
done
for i in {1..3}
do
	python -m main @scripts/args_anymal.txt --logdir_suffix Ensemble --seed $i --order UC --network base
done
for i in {1..3}
do
	python -m main @scripts/args_allegro.txt --logdir_suffix Ensemble --seed $i --order UC --network base
done

for i in {1..3}
do
	python -m main @scripts/args_humanoid.txt --logdir_suffix Ensemble --seed $i --order UC --network real
done
for i in {1..3}
do
	python -m main @scripts/args_anymal.txt --logdir_suffix Ensemble --seed $i --order UC --network real
done
for i in {1..3}
do
	python -m main @scripts/args_allegro.txt --logdir_suffix Ensemble --seed $i --order UC --network real
done

for i in {1..3}
do
	python -m main @scripts/args_humanoid.txt --logdir_suffix Ensemble --seed $i --order UC --network dirichlet
done
for i in {1..3}
do
	python -m main @scripts/args_anymal.txt --logdir_suffix Ensemble --seed $i --order UC --network dirichlet
done
for i in {1..3}
do
	python -m main @scripts/args_allegro.txt --logdir_suffix Ensemble --seed $i --order UC --network dirichlet
done



