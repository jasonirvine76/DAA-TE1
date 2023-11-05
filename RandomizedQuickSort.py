import random
import pickle
import time
import os
import psutil
import tracemalloc
from memory_profiler import memory_usage, profile
import sys
sys.setrecursionlimit(131072)
'''
The function which implements QuickSort using Lomuto Partition.
arr :- array to be sorted.
start :- starting index of the array.
stop :- ending index of the array.
'''

"""Source: https://www.geeksforgeeks.org/quicksort-using-random-pivoting/"""
def quicksort(arr, start , stop):
    if(start < stop):
         
        # pivot_index is the index where 
        # the pivot lies in the array
        pivot_index = partition_rand(arr,\
                             start, stop)
         
        # At this stage the array is 
        # partially sorted around the pivot. 
        # Separately sorting the 
        # left half of the array and the
        # right half of the array.
        quicksort(arr , start , pivot_index-1)
        quicksort(arr, pivot_index + 1, stop)
 
# This function generates random pivot,
# swaps the first element with the pivot 
# and calls the partition function.
def partition_rand(arr , start, stop):
 
    # Generating a random number between the 
    # starting index of the array and the
    # ending index of the array.
    randpivot = random.randrange(start, stop)
 
    # Swapping the starting element of
    # the array and the pivot
    arr[start], arr[randpivot] = arr[randpivot], arr[start]
    return partition(arr, start, stop)
 
'''
This function takes the first element as pivot, 
places the pivot element at the correct position 
in the sorted array. All the elements are re-arranged 
according to the pivot, the elements smaller than the
pivot is places on the left and the elements
greater than the pivot is placed to the right of pivot.
'''
def partition(arr,start,stop):
    pivot = start # pivot
     
    # a variable to memorize where the 
    i = start + 1
     
    # partition in the array starts from.
    for j in range(start + 1, stop + 1):
         
        # if the current element is smaller
        # or equal to pivot, shift it to the
        # left side of the partition.
        if arr[j] <= arr[pivot]:
            arr[i] , arr[j] = arr[j] , arr[i]
            i = i + 1
    arr[pivot] , arr[i - 1] = arr[i - 1] , arr[pivot]
    pivot = i - 1
    return (pivot)
def process_memory():
    process = psutil.Process(os.getpid())
    mem_info = process.memory_info()
    return mem_info.rss
# Driver Code

if __name__ == "__main__":
    array = [5, 3, 7, 7, 2, 8, 4, 1]
    quicksort(array, 0, len(array) - 1)
    print(array)
    
    print("Hasil eksperimen dari algoritma Randomized Quick Sort")
    for filename in os.listdir("dataset"):
        if filename.endswith(".pkl"):
            dataset_name = os.path.join("dataset", filename)
            with open(dataset_name, 'rb') as file:
                dataset = pickle.load(file)
            print(f"Dataset from {dataset_name}:")
            start_time = time.perf_counter()
            sorted_dataset = quicksort(dataset, 0, len(dataset)-1)
            end_time = time.perf_counter()
            mem_usage = memory_usage((quicksort, (dataset,0,len(dataset)-1)), interval=0.1, timeout=200)
            execution_time = (end_time - start_time)
            print(f"Penggunaan Memori Selama Eksekusi: {max(mem_usage)} MiB")
            print(f"Execution time for {dataset_name}: {execution_time} seconds\n")


            