from arg_utils import get_parser
import os.path as osp
from iflb.parallel_experiment_optuna import ParallelExperiment
from iflb.agents import *
from iflb.supervisors import *
from iflb.allocations import *
from iflb.networks import *
from dotmap import DotMap
import yaml
import optuna
from functools import partial
import optuna_main
from hydra.core.global_hydra import GlobalHydra
from hydra import initialize, initialize_config_module, compose
from joblib import Parallel, delayed
import subprocess
import json 
import os
import base64
import pickle

def update_args_(args, params):
        dargs = vars(args)
        dargs.update(params)

def optimize():
    
    def objective(trial):
        
        trial_number = trial.number

        params_to_optimize = {
                'logdir_suffix': 'trial' + str(trial_number), 
                "uncertainty_thresh": trial.suggest_float("uncertainty_thresh", 0, 1),
                "risk_thresh": trial.suggest_float("risk_thresh", 0, 1),
            }

        exp_cfg, agent, supervisor, allocation, network = optuna_main.main(
             num_envs=None,
             num_humans=None,
             allocation_name="CUR"
            )

        print(exp_cfg)
        update_args_(exp_cfg, params_to_optimize) 
        exp_cfg.allocation_cfg.uncertainty_thresh = params_to_optimize["uncertainty_thresh"]
        exp_cfg.allocation_cfg.risk_thresh = params_to_optimize["risk_thresh"]
        print(exp_cfg)
        
        experiment = ParallelExperiment(exp_cfg, agent, supervisor, allocation, network)
        success, rohe = experiment.run()
        
        return success, rohe

    storage_url = "sqlite:///optim_results.db"
    study_name = "rev_scarce_anymal"
    study = optuna.create_study(
        study_name=study_name,
        storage=storage_url,
        load_if_exists=True,
        directions=["maximize", "maximize"],
        sampler=optuna.samplers.RandomSampler()
    )

    study.optimize(objective, n_trials=1)

if __name__ == "__main__":
    optimize()

