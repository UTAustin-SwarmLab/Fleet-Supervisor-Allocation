# Fleet-Supervisor-Allocation

This repository covers the implementation of the Fleet Supervisor Allocation Problem where we use the notion of Submodularity to solve the problem. 

## Packages 

For the installation of the required packages and datasets, please first create a virtual environment and then run the following command:

```bash
conda create -n fsa python=3.8.18
```

Then, activate the virtual environment:

```bash
conda activate fsa
```

To run the IFLB you will need to install Isaac Gym. Download Isaac Gym 1.0rc3 from https://developer.nvidia.com/isaac-gym (you may need to send a request but it should be quickly approved) and read the installation instructions in the docs to pip install into the virtual environment. You will need NVIDIA driver version >= 470.



This repository uses poetry for package management. Please install poetry using the following command:

```bash
pip3 install poetry
```

Then, you can install the required packages using the following command:

```bash
poetry lock && poetry install
```




The extension of the Fleet Supervisor Allocation Problem, in here the problem is extended to include the uncertainity in the allocation being unsuccesful. The problem is solved using a Adaptive Submodularity based algorithm. The algorithm and the other approaches are compared and the results are presented in the paper.

This repo is created on the following repository: Fleet-Dagger.


