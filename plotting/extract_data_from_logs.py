import os
import pickle
from tqdm import tqdm

def extract_data_from_logs(
        logs_dir: str,
        metrics_to_extract: list,
        allocation_policies: list,
        environments: list,
        networks: list,  
    ) -> list:
    
    

    # Read the logs and extract and save the data to npz files for each metric and allocation policy

    logs = []

    # Go over each run_stats.pkl file given in the logs directory and its subdirectories
    # If ablation studies pass it



    for root, dirs, files in os.walk(logs_dir):
        for file in files:
            if "ablation_studies" in root:
                continue
            if file == "run_stats.pkl":
                log = os.path.join(root, file)
                logs.append(log)

    data_to_be_saved = []

    pbar = tqdm(logs, desc="Extracting data from logs")

    for log in pbar:

        log_allocation_policy = ""
        log_env = ""
        log_network = ""

        for policy in allocation_policies:
            if policy.lower() in log.lower():
                log_allocation_policy = policy
                break
        
        for env in environments:
            if env.lower() in log.lower():
                log_env = env
                break
        
        for network in networks:
            if network.lower() in log.lower():
                log_network = network
                break
        
        if log_allocation_policy == "" or log_env == "" or log_network == "":
            continue

        # Load the data from the log file

        data = pickle.load(open(log, "rb"))

        # Extract the data for each metric
        
        for metric in metrics_to_extract:

            metric_data = data[metric]

            if metric == "ROHE":
                metric_data = [d * 100 for d in metric_data]

            data_to_be_saved.append({"allocation_policy": log_allocation_policy, "env": log_env, "network": log_network, "metric": metric, "data": metric_data})

    return data_to_be_saved
