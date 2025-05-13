import matplotlib.pyplot as plt
import numpy as np
import time
from quick_sort import shuffled_quick_sort
from merge_sort import merge_sort
from insertion_sort import insertion_sort
from test_cases import test_arrays
from quick_sort_no_shuffle import quick_sort as quick_sort_no_shuffle

def measure_sorting_time(sort_func, arr):
    arr_copy = arr.copy()
    start_time = time.time()
    sort_func(arr_copy)
    return time.time() - start_time

def create_performance_visualization():
    # Prepare data
    algorithms = ['Quick Sort', 'Merge Sort', 'Insertion Sort']
    test_cases = list(test_arrays.keys())
    
    # Initialize results matrix
    results = np.zeros((len(algorithms), len(test_cases)))
    
    # Measure performance for each algorithm and test case
    for i, (case_name, arr) in enumerate(test_arrays.items()):
        results[0, i] = measure_sorting_time(shuffled_quick_sort, arr)
        results[1, i] = measure_sorting_time(merge_sort, arr)
        results[2, i] = measure_sorting_time(insertion_sort, arr)
    
    # Create bar chart
    plt.figure(figsize=(15, 8))
    x = np.arange(len(test_cases))
    width = 0.25
    
    for i, algorithm in enumerate(algorithms):
        plt.bar(x + i*width, results[i], width, label=algorithm)
    
    plt.xlabel('Test Cases')
    plt.ylabel('Time (seconds)')
    plt.title('Sorting Algorithms Performance Comparison')
    plt.xticks(x + width, test_cases, rotation=45)
    plt.legend()
    plt.tight_layout()
    
    # Save the plot
    plt.savefig('sorting_performance.png')
    plt.close()

def create_time_comparison_plot():
    # Test with different array sizes
    sizes = [100, 500, 1000, 2000, 5000]
    algorithms = {
        'Quick Sort': shuffled_quick_sort,
        'Merge Sort': merge_sort,
        'Insertion Sort': insertion_sort
    }
    
    results = {name: [] for name in algorithms.keys()}
    
    for size in sizes:
        # Create random array of given size
        arr = [np.random.randint(1, 1000) for _ in range(size)]
        
        for name, sort_func in algorithms.items():
            time_taken = measure_sorting_time(sort_func, arr)
            results[name].append(time_taken)
    
    # Create line plot
    plt.figure(figsize=(10, 6))
    for name, times in results.items():
        plt.plot(sizes, times, marker='o', label=name)
    
    plt.xlabel('Array Size')
    plt.ylabel('Time (seconds)')
    plt.title('Sorting Algorithms Performance vs Array Size')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    
    # Save the plot
    plt.savefig('sorting_time_comparison.png')
    plt.close()

if __name__ == "__main__":
    create_performance_visualization()
    create_time_comparison_plot()
    print("Visualizations have been created and saved as 'sorting_performance.png' and 'sorting_time_comparison.png'") 