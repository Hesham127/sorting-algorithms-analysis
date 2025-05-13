def quick_sort(arr):
    # Base case: if array has 1 or 0 elements, it's already sorted
    if len(arr) <= 1:
        return arr
    else:
        # Choose the first element as pivot
        pivot = arr[0]
        # Subarray of elements less than or equal to pivot
        less = [x for x in arr[1:] if x <= pivot]
        # Subarray of elements greater than pivot
        greater = [x for x in arr[1:] if x > pivot]
        # Recursively sort and concatenate
        return quick_sort(less) + [pivot] + quick_sort(greater) 