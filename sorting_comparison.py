import random
import time
import sys
from quick_sort import shuffled_quick_sort
from merge_sort import merge_sort
from insertion_sort import insertion_sort
from test_cases import test_arrays
from quick_sort_no_shuffle import quick_sort as quick_sort_no_shuffle

sys.setrecursionlimit(2000)

def main():
    print("Comparing sorting algorithms on predefined test cases:\n")
    for case_name, arr in test_arrays.items():
        print(f"Test case: {case_name} (size: {len(arr)})")
        # Quick Sort (shuffled)
        arr_copy = arr.copy()
        start_time = time.time()
        shuffled_quick_sort(arr_copy)
        quick_time = time.time() - start_time
        # Merge Sort
        arr_copy = arr.copy()
        start_time = time.time()
        merge_sort(arr_copy)
        merge_time = time.time() - start_time
        # Insertion Sort
        arr_copy = arr.copy()
        start_time = time.time()
        insertion_sort(arr_copy)
        insertion_time = time.time() - start_time
        # Quick Sort (no shuffle) only for sorted and reverse_sorted
        if case_name in ["sorted", "reverse_sorted"]:
            arr_copy = arr.copy()
            start_time = time.time()
            quick_sort_no_shuffle(arr_copy)
            no_shuffle_time = time.time() - start_time
            print(f"  Quick Sort (no shuffle) time: {no_shuffle_time:.6f} seconds")
        # Print results
        print(f"  Quick Sort (shuffled) time: {quick_time:.6f} seconds")
        print(f"  Merge Sort time: {merge_time:.6f} seconds")
        print(f"  Insertion Sort time: {insertion_time:.6f} seconds\n")

if __name__ == "__main__":
    main()
