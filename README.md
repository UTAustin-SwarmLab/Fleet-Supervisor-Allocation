# Fleet-Supervisor-Allocation

The extension of the Fleet Supervisor Allocation Problem, in here the problem is extended to include the uncertainity in the allocation being unsuccesful. The problem is solved using a Adaptive Submodularity based algorithm. The algorithm and the other approaches are compared and the results are presented in the paper.

This repo is created on the following repository: Fleet-Dagger.


## Installation and Setup
------------
To manage dependencies and packages we use conda. Please make sure you have conda installed on your system. Additionally please download the Isaac Gym 1.0rc4 https://developer.nvidia.com/isaac-gym (you may need to send a request but it should be quickly approved) and place it under the isaacgym folder.  

After cloning the repository, if it didn't initalized the submodules please run the following command:
```bash
git submodule update --init
```

Then you can create the conda environment by running the following command and activate it:
```bash
conda env create -f environment.yml
conda activate fsa
```

Then you can install the Isaac Gym and the IsaacGym Environment by running the following commands:
```bash
cd isaacgym/python
pip install -e .
cd ../../IsaacGymEnvs
pip install -e .
```

## Running the Code
----------------------

Below runs all allocation policies for each task with 3 different seeds each. To change the network configuration of the environment change the `network_type` variable.

### Humanoid
`. scripts/run_humanoid.sh`

## Allegro Hand
`. scripts/run_allegro.sh`

## Anymal
`. scripts/run_anymal.sh`

## Ball Balance
`. scripts/run_ballbalance.sh`

## Generating Plots
----------------------
All experiment logs are saved to `logs/`. The logs should be organized in a way that (1) for each task there exists a folder (e.g. `logs/humanoid`); (2) in each "task" folder there should be allocation results and each allocation should have three seeds (if you want to try more or fewer seeds modify lines 89 and 90 in the `plotting/plot.py` file). To plot; run `python plotting/plot.py logs/humanoid [METRIC]`, where metric is ROHE, cumulative_successes or something else.