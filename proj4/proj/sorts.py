"""
This program defines various sorts

__author__ = Alex Shah
__version__ = proj4
"""


def quicksort_first_pivot(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quicksort_first_pivot(arr, low, pi - 1)
        quicksort_first_pivot(arr, pi + 1, high)


def partition(arr, low, high):
    pivot = arr[low]
    i = low + 1
    for j in range(low + 1, high + 1):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[low], arr[i - 1] = arr[i - 1], arr[low]
    return i - 1


def quicksort_with_insertion(arr, low, high, threshold=100):
    if high - low <= threshold:
        insertion_sort(arr, low, high)
    else:
        if low < high:
            pi = partition(arr, low, high)
            quicksort_with_insertion(arr, low, pi - 1, threshold)
            quicksort_with_insertion(arr, pi + 1, high, threshold)


def insertion_sort(arr, low, high):
    for i in range(low + 1, high + 1):
        key = arr[i]
        j = i - 1
        while j >= low and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def quicksort_median_pivot(arr, low, high):
    if low < high:
        pi = partition_median(arr, low, high)
        quicksort_median_pivot(arr, low, pi - 1)
        quicksort_median_pivot(arr, pi + 1, high)


def partition_median(arr, low, high):
    mid = (low + high) // 2
    if arr[low] > arr[mid]:
        arr[low], arr[mid] = arr[mid], arr[low]
    if arr[low] > arr[high]:
        arr[low], arr[high] = arr[high], arr[low]
    if arr[mid] > arr[high]:
        arr[mid], arr[high] = arr[high], arr[mid]
    arr[mid], arr[high - 1] = arr[high - 1], arr[mid]
    return partition(arr, low, high - 1)


# Outline for Natural Merge Sort
class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


def natural_merge_sort(head):
    # todo
    pass
