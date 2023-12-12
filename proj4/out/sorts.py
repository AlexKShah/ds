"""
This program defines 5 sorts
Quicksort
  - First item pivot
  - Insert <= 100
  - Insert <= 50
  - Median of three
Natural Merge Sort

__author__ = Alex Shah
__version__ = proj4
"""

from proj.mystack import *


def partition_first(arr, low, high):
    comparisons, exchanges = 0, 0
    pivot = arr[low]
    i = low + 1

    for j in range(low + 1, high + 1):
        comparisons += 1
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            exchanges += 1
            i += 1

    arr[low], arr[i - 1] = arr[i - 1], arr[low]
    exchanges += 1
    return i - 1, comparisons, exchanges


def insertion_sort(arr, low, high):
    comparisons, exchanges = 0, 0
    for i in range(low + 1, high + 1):
        key = arr[i]
        j = i - 1

        while j >= low:
            comparisons += 1
            if arr[j] > key:
                arr[j + 1] = arr[j]
                exchanges += 1
                j -= 1
            else:
                break

        arr[j + 1] = key
        exchanges += 1

    return arr, comparisons, exchanges


def merge_sorted_lists(left, right):
    dummy = tail = ListNode()
    comparisons, exchanges = 0, 0

    while left and right:
        comparisons += 1
        if left.value < right.value:
            tail.next = left
            left = left.next
        else:
            tail.next = right
            right = right.next
        exchanges += 1
        tail = tail.next

    tail.next = left or right
    exchanges += 1 if tail.next else 0

    return dummy.next, comparisons, exchanges


def partition_median(arr, low, high):
    comparisons, exchanges = 0, 0

    # Finding the median of the first, middle, and last elements
    mid = low + (high - low) // 2
    if arr[mid] < arr[low]:
        arr[mid], arr[low] = arr[low], arr[mid]
        exchanges += 1
    if arr[high] < arr[low]:
        arr[high], arr[low] = arr[low], arr[high]
        exchanges += 1
    if arr[mid] < arr[high]:
        arr[mid], arr[high] = arr[high], arr[mid]
        exchanges += 1

    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        comparisons += 1
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            exchanges += 1

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    exchanges += 1

    return i + 1, comparisons, exchanges


def quicksort_first_pivot(arr):
    stack = MyStack()
    stack.push((0, len(arr) - 1))
    total_comp, total_exch = 0, 0

    while not stack.is_empty():
        start, end = stack.pop()
        if start < end:
            pivot_index, comp, exch = partition_first(arr, start, end)
            total_comp += comp
            total_exch += exch

            # Push indices of subarrays onto stack
            stack.push((start, pivot_index - 1))
            stack.push((pivot_index + 1, end))

    return arr, total_comp, total_exch


def quicksort_insertion_100(arr, low, high):
    return quicksort_insertion(arr, low, high, 100)


def quicksort_insertion_50(arr, low, high):
    return quicksort_insertion(arr, low, high, 50)


def quicksort_insertion(arr, low, high, threshold):
    comp, exch = 0, 0
    stack = [(low, high)]

    while stack:
        low, high = stack.pop()
        if high - low <= threshold:
            _, insert_comp, insert_exch = insertion_sort(arr, low, high)
            comp += insert_comp
            exch += insert_exch
        elif low < high:
            pivot_index, pivot_comp, pivot_exch = partition_first(arr, low, high)
            comp += pivot_comp
            exch += pivot_exch

            stack.append((low, pivot_index - 1))
            stack.append((pivot_index + 1, high))

    return arr, comp, exch


def quicksort_median_pivot(arr, low, high):
    comp, exch = 0, 0
    stack = [(low, high)]

    while stack:
        low, high = stack.pop()
        if low < high:
            pivot_index, pivot_comp, pivot_exch = partition_median(arr, low, high)
            comp += pivot_comp
            exch += pivot_exch

            stack.append((low, pivot_index - 1))
            stack.append((pivot_index + 1, high))

    return arr, comp, exch


def natural_merge_sort(head):
    comparisons, exchanges = 0, 0
    if head is None or head.next is None:
        return head, comparisons, exchanges

    size = 1
    while True:
        left = head
        prev_tail = dummy = ListNode()
        num_merges = 0

        while left:
            num_merges += 1
            right = split_list_at(left, size)
            left_next = split_list_at(right, size)

            merged, merge_comp, merge_exch = merge_sorted_lists(left, right)
            comparisons += merge_comp
            exchanges += merge_exch

            prev_tail.next = merged
            while prev_tail.next:
                prev_tail = prev_tail.next

            left = left_next

        head = dummy.next
        if num_merges <= 1:
            break
        size *= 2

    return head, comparisons, exchanges


def split_list_at(head, size):
    while size - 1 > 0 and head:
        head = head.next
        size -= 1
    if not head:
        return None
    next_head = head.next
    head.next = None
    return next_head
