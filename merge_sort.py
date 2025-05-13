def merge_sort(arr):
    # Base case: if array has 1 or 0 elements, it's already sorted
    if len(arr) <= 1:
        return arr
    
    # Find middle point to divide array into two halves
    mid = len(arr) // 2  # Fixed: divide by 2 to get the middle point
    
    # Recursively sort first and second halves
    left = merge_sort(arr[:mid])   # Sort left half
    right = merge_sort(arr[mid:])  # Sort right half
    
    # Merge the sorted halves
    return merge(left, right)

# Helper function to merge two sorted arrays
def merge(left, right):
    result = []  # Initialize empty result array
    i = j = 0    # Initialize pointers for both arrays
    
    # Compare elements from both arrays and merge them in sorted order
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])  # Add element from left array
            i += 1                  # Move left array pointer
        else:
            result.append(right[j]) # Add element from right array
            j += 1                  # Move right array pointer
    
    # Add remaining elements from left array, if any
    result.extend(left[i:])
    # Add remaining elements from right array, if any
    result.extend(right[j:])
    
    return result  # Return merged sorted array