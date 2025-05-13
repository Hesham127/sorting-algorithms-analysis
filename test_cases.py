import random

test_arrays = {
    "sorted": [i for i in range(1, 1001)],  # Sorted 1 to 1000
    "reverse_sorted": [i for i in range(1000, 0, -1)],  # Reverse sorted 1000 to 1
    "mixed": [random.randint(1, 1000) for _ in range(1000)],  # 1000 mixed values
    "duplicates": [random.choice([4, 7, 1, 9, 3, 2]) for _ in range(1000)],  # 1000 items with duplicates
    "empty": [],  # Empty list
    "single_element": [42],  # One element
    "large_random": [random.randint(1, 1000) for _ in range(1000)],  # 1000 random integers
    "nearly_sorted": [i if i % 10 != 0 else i - 3 for i in range(1, 1001)],  # Small perturbations in otherwise sorted list
}
