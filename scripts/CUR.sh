for i in {1..5}
do
	python -m main @scripts/args_humanoid.txt --logdir_suffix CUR --seed $i --warmup_penalty 1000 -network real
done
for i in {1..5}
do
	python -m main @scripts/args_anymal.txt --logdir_suffix CUR --seed $i --warmup_penalty 250 -network real
done
for i in {1..5}
do
	python -m main @scripts/args_allegro.txt --logdir_suffix CUR --seed $i --warmup_penalty 2500 -network real
done

for i in {1..5}
do
	python -m main @scripts/args_humanoid.txt --logdir_suffix CUR --seed $i --warmup_penalty 1000 -network base
done
for i in {1..5}
do
	python -m main @scripts/args_anymal.txt --logdir_suffix CUR --seed $i --warmup_penalty 250 -network base
done
for i in {1..5}
do
	python -m main @scripts/args_allegro.txt --logdir_suffix CUR --seed $i --warmup_penalty 2500 -network base
done

for i in {1..5}
do
	python -m main @scripts/args_humanoid.txt --logdir_suffix CUR --seed $i --warmup_penalty 1000 -network dirichlet
done
for i in {1..5}
do
	python -m main @scripts/args_anymal.txt --logdir_suffix CUR --seed $i --warmup_penalty 250 -network dirichlet
done
for i in {1..5}
do
	python -m main @scripts/args_allegro.txt --logdir_suffix CUR --seed $i --warmup_penalty 2500 -network dirichlet
done

