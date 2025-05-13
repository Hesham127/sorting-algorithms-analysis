
import random

def quick_sort(arr):
    # Base case: if array has 1 or 0 elements, it's already sorted
    if len(arr) <= 1:
        return arr
    else:
        # Choose the first element as pivot
        pivot = arr[0]

        #Subarray of elements less than or equal to pivot
        less = [x for x in arr[1:] if x <= pivot]

        #Subarray of elements greater than pivot
        greater = [x for x in arr[1:] if x > pivot]

        # Recursively sort and concatenate
        return quick_sort(less) + [pivot] + quick_sort(greater)

def shuffled_quick_sort(arr):
    # Create a copy to avoid modifying the original list
    arr_copy = arr[:]
    random.shuffle(arr_copy)
    return quick_sort(arr_copy)

# Example usage:
arr = [3, 6, 8, 10, 1, 2, 1]
sorted_arr = shuffled_quick_sort(arr)
print(sorted_arr)  # Output: [1, 1, 2, 3, 6, 8, 10]
