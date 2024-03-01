for i in {1..5}
do
python -m main @scripts/args_humanoid.txt --logdir_suffix ASM --allocation ASM --seed $i --std_dev 0.05 --action_budget 20000 --network real 
done
for i in {1..5}
do
	python -m main @scripts/args_allegro.txt --logdir_suffix ASM --allocation ASM --seed $i --action_budget 19000 --network real
done
for i in {1..5}
do
	python -m main @scripts/args_anymal.txt --logdir_suffix ASM --allocation ASM --seed $i --std_dev 0.05 --action_budget 4000 --network real
done

for i in {1..5}
do
python -m main @scripts/args_humanoid.txt --logdir_suffix ASM --allocation ASM --seed $i --std_dev 0.05 --action_budget 20000 --network base 
done
for i in {1..5}
do
	python -m main @scripts/args_allegro.txt --logdir_suffix ASM --allocation ASM --seed $i --action_budget 19000 --network base
done
for i in {1..5}
do
	python -m main @scripts/args_anymal.txt --logdir_suffix ASM --allocation ASM --seed $i --std_dev 0.05 --action_budget 4000 --network base
done

for i in {1..5}
do
python -m main @scripts/args_humanoid.txt --logdir_suffix ASM --allocation ASM --seed $i --std_dev 0.05 --action_budget 20000 --network dirichlet
done
for i in {1..5}
do
	python -m main @scripts/args_allegro.txt --logdir_suffix ASM --allocation ASM --seed $i --action_budget 19000 --network dirichlet
done
for i in {1..5}
do
	python -m main @scripts/args_anymal.txt --logdir_suffix ASM --allocation ASM --seed $i --std_dev 0.05 --action_budget 4000 --network dirichlet
done