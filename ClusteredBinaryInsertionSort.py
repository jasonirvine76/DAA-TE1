import pickle
import time
import os
from tracemalloc import start
import psutil
from memory_profiler import memory_usage
import sys
sys.setrecursionlimit(131072)

def binary_loc_finder(a_list, start, end, key):
    if start == end:
        if a_list[start] > key:
            loc = start
            return loc
        else:
            loc = start + 1
            return loc
    if start > end:
        loc = start
        return loc
    else:
        middle = (start + end) // 2
        if a_list[middle] < key:
            return binary_loc_finder(a_list, middle + 1, end, key)
        elif a_list[middle] > key:
            return binary_loc_finder(a_list, start, middle - 1, key)
        else:
            return middle

def place_inserter(a_list, start, end):
    temp = a_list[end]
    k = end
    while k > start:
        a_list[k] = a_list[k - 1]
        k -= 1
    a_list[start] = temp
    return a_list

def sort_list(a_list):
    pop = 0
    for i in range(1, len(a_list)):
        cop = i
        key = a_list[cop]
        if key >= a_list[pop]:
            place = binary_loc_finder(a_list, pop + 1, cop - 1, key)
        else:
            place = binary_loc_finder(a_list, 0, pop - 1, key)
        position = place
        a_list = place_inserter(a_list, place, cop)
    return a_list



# Example usage
if __name__ == '__main__':
    a_list = [5, 3, 7, 7, 2, 8, 4, 1]
    sorted_list = sort_list(a_list)
    print(sorted_list)

    print("Hasil eksperimen dari algoritma Clustered Binary Insertion Sort")
    for filename in os.listdir("dataset"):
            if filename.endswith(".pkl"):
                dataset_name = os.path.join("dataset", filename)
                with open(dataset_name, 'rb') as file:
                    dataset = pickle.load(file)
                print(f"Dataset from {dataset_name}:")
                start_time = time.perf_counter()
                sorted_dataset = sort_list(dataset)
                end_time = time.perf_counter()
                mem_usage = memory_usage((sort_list, (dataset,)), interval=0.1, timeout=200)
                execution_time = (end_time - start_time)
                print(f"Penggunaan Memori Selama Eksekusi: {max(mem_usage)} MiB")
                print(f"Execution time for {dataset_name}: {execution_time} seconds\n")