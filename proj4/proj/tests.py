"""
Tests and runner for proj4
Create test files with different sizes and orders
to run 5 sorts against them
= 75 runs

__author__ = Alex Shah
__version__ = proj4
"""

import random
import os
from proj.sorts import *


def create_output_directory():
    os.makedirs('proj/output_files', exist_ok=True)


def write_to_file(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)


def create_input_files(sizes):
    os.makedirs('proj/input_files', exist_ok=True)
    for size in sizes:
        try:
            # Random order
            with open(f'proj/input_files/input_random_{size}.txt', 'w') as file:
                numbers = [random.randint(1, size * 100) for _ in range(size)]
                file.write('\n'.join(map(str, numbers)))

            # Ascending order
            with open(f'proj/input_files/input_ascending_{size}.txt', 'w') as file:
                numbers = list(range(1, size + 1))
                file.write('\n'.join(map(str, numbers)))

            # Descending order
            with open(f'proj/input_files/input_descending_{size}.txt', 'w') as file:
                numbers = list(range(size, 0, -1))
                file.write('\n'.join(map(str, numbers)))
        except Exception as e:
            print(f"Error in {file}: {e}")


def array_to_linked_list(arr):
    if not arr:
        return None
    head = tail = ListNode(arr[0])
    for value in arr[1:]:
        tail.next = ListNode(value)
        tail = tail.next
    return head


def linked_list_to_array(head):
    arr = []
    current = head
    while current:
        arr.append(current.value)
        current = current.next
    return arr


def run_sorts():
    sizes = [50, 1000, 2000, 5000, 10000]
    orders = ['random', 'ascending', 'descending']
    sorting_functions = [
        quicksort_first_pivot, quicksort_insertion_100, quicksort_insertion_50,
        quicksort_median_pivot, natural_merge_sort
    ]

    create_input_files(sizes)
    create_output_directory()

    for size in sizes:
        for order in orders:
            file_path = f'proj/input_files/input_{order}_{size}.txt'
            with open(file_path, 'r') as file:
                data = [int(line.strip()) for line in file]

            for sort_function in sorting_functions:
                try:
                    copied_data = data.copy()
                    if sort_function == natural_merge_sort:
                        # Convert array to linked list for natural merge sort
                        head = array_to_linked_list(copied_data)
                        head, comparisons, exchanges = sort_function(head)
                        sorted_data = linked_list_to_array(head)  # Convert back to array after sorting
                    else:
                        # Adjust call for quicksort_first_pivot having 1 param
                        if sort_function == quicksort_first_pivot:
                            sorted_data, comparisons, exchanges = sort_function(copied_data)
                        else:
                            sorted_data, comparisons, exchanges = sort_function(copied_data, 0, len(copied_data) - 1)
                    output_file_path = f'proj/output_files/output_{sort_function.__name__}_{order}_{size}.txt'
                    output_content = f"Sort: {sort_function.__name__}, Order: {order}, Size: {size}\n"
                    if size == 50:
                        output_content += "Sorted Data: " + ', '.join(map(str, sorted_data)) + '\n'
                    output_content += f"Comparisons: {comparisons}, Exchanges: {exchanges}\n"
                    write_to_file(output_file_path, output_content)

                except Exception as e:
                    print(f"Error in {sort_function.__name__}, {order}, Size {size}: {e}")


if __name__ == "__main__":
    run_sorts()
