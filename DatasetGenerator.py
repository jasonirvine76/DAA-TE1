import random
import pickle

def generate_dataset(size, status):
    if status == "sorted":
        dataset = list(range(size))
    elif status == "random":
        dataset = random.sample(range(size), size)
    elif status == "reversed":
        dataset = list(range(size, 0, -1))
    else:
        raise ValueError("Status harus berupa 'sorted', 'random', atau 'reversed'.")

    return dataset

sizes = [200, 2000, 20000]
statuses = ["sorted", "random", "reversed"]

# Generate dataset 
for size in sizes:
    for status in statuses:
        dataset = generate_dataset(size, status)
        dataset_name = f"dataset/dataset_{size}_{status}.pkl"
        with open(dataset_name, 'wb') as file:
            pickle.dump(dataset, file)