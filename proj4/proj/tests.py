import random
import os
from sorts import *


def create_input_files(sizes):
    os.makedirs('input_files', exist_ok=True)
    for size in sizes:
        # Random order
        with open(f'input_files/input_random_{size}.txt', 'w') as file:
            numbers = [random.randint(1, size * 100) for _ in range(size)]
            file.write('\n'.join(map(str, numbers)))

        # Ascending order
        with open(f'input_files/input_ascending_{size}.txt', 'w') as file:
            numbers = list(range(1, size + 1))
            file.write('\n'.join(map(str, numbers)))

        # Descending order
        with open(f'input_files/input_descending_{size}.txt', 'w') as file:
            numbers = list(range(size, 0, -1))
            file.write('\n'.join(map(str, numbers)))


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
    create_input_files(sizes)
    sorting_functions = [
        quicksort_first_pivot, quicksort_insertion_100, quicksort_insertion_50,
        quicksort_median_pivot, natural_merge_sort
    ]

    for size in sizes:
        for order in ['random', 'ascending', 'descending']:
            file_path = f'input_files/input_{order}_{size}.txt'
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
                        sorted_data, comparisons, exchanges = sort_function(copied_data, 0, len(copied_data) - 1)

                    if size == 50:
                        # Print sorted data and counts for size 50
                        print(f"\n{sort_function.__name__}, {order}, Size {size}:")
                        print("Sorted Data:", sorted_data)
                    print(f"Comparisons: {comparisons}, Exchanges: {exchanges}")

                except Exception as e:
                    print(f"Error in {sort_function.__name__}, {order}, Size {size}: {e}")


if __name__ == "__main__":
    run_sorts()
