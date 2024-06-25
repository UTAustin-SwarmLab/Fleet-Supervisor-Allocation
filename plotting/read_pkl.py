import pickle
import sys

cfg_dir = sys.argv[1]

def read_pkl_file(cfg_dir):
    with open(cfg_dir, "rb") as file:
        env_configs = pickle.load(file)
    return env_configs

if __name__ == "__main__":
    env_configs = read_pkl_file(cfg_dir)
    print(env_configs)