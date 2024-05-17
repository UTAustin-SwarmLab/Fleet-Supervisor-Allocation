import pickle

directory = '/home/oguzhan-admin/Fleet-Supervisor-Allocation/logs/Anymal_final_experiments/base/2024-05-14_01-18-25_Anymal_random/args.pkl'
with open(directory, 'rb') as file:
    data = pickle.load(file)

print(data)
