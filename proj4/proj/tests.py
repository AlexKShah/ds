from sorts import quicksort_first_pivot, quicksort_with_insertion, quicksort_median_pivot
import random
import time


def generate_test_data(size, order='random'):
    if order == 'random':
        return [random.randint(1, 10000) for _ in range(size)]
    elif order == 'reverse':
        return list(range(size, 0, -1))
    elif order == 'sorted':
        return list(range(1, size + 1))


def test_sort_function(sort_function, data):
    start_time = time.time()
    sort_function(data, 0, len(data) - 1)
    end_time = time.time()
    return end_time - start_time


def run_sorting_tests():
    for size in [50, 1000, 2000, 5000, 10000]:
        for order in ['random', 'reverse', 'sorted']:
            data = generate_test_data(size, order)
            time_taken = test_sort_function(quicksort_first_pivot, data.copy())
            print(f"Quicksort (First Pivot) - Size: {size}, Order: {order}, Time: {time_taken:.4f}s")
            # Repeat for other sorting functions and analyze performance


if __name__ == "__main__":
    run_sorting_tests()
