"""
This program defines various sorts

__author__ = Alex Shah
__version__ = proj4
"""


class SortResult:
    def __init__(self, sorted_data, comparisons, exchanges):
        self.sorted_data = sorted_data
        self.comparisons = comparisons
        self.exchanges = exchanges


class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


def quicksort_first_pivot(arr, low, high, comparisons=0, exchanges=0):
    if low < high:
        pivot_index, comp, exch = partition_first(arr, low, high)
        comparisons += comp
        exchanges += exch

        arr, comp, exch = quicksort_first_pivot(arr, low, pivot_index - 1, comparisons, exchanges)
        comparisons += comp
        exchanges += exch

        arr, comp, exch = quicksort_first_pivot(arr, pivot_index + 1, high, comparisons, exchanges)
        comparisons += comp
        exchanges += exch

    return arr, comparisons, exchanges


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


def quicksort_insertion_100(arr, low, high, comparisons=0, exchanges=0):
    if high - low <= 100:
        arr, comp, exch = insertion_sort(arr, low, high)
        return arr, comparisons + comp, exchanges + exch
    else:
        pivot_index, comp, exch = partition_first(arr, low, high)
        comparisons += comp
        exchanges += exch
        arr, comp, exch = quicksort_insertion_100(arr, low, pivot_index - 1, comparisons, exchanges)
        comparisons += comp
        exchanges += exch
        arr, comp, exch = quicksort_insertion_100(arr, pivot_index + 1, high, comparisons, exchanges)
        comparisons += comp
        exchanges += exch
        return arr, comparisons, exchanges


def quicksort_insertion_50(arr, low, high, comparisons=0, exchanges=0):
    if high - low <= 50:
        arr, comp, exch = insertion_sort(arr, low, high)
        return arr, comparisons + comp, exchanges + exch
    else:
        pivot_index, comp, exch = partition_first(arr, low, high)
        comparisons += comp
        exchanges += exch
        arr, comp, exch = quicksort_insertion_50(arr, low, pivot_index - 1, comparisons, exchanges)
        comparisons += comp
        exchanges += exch
        arr, comp, exch = quicksort_insertion_50(arr, pivot_index + 1, high, comparisons, exchanges)
        comparisons += comp
        exchanges += exch
        return arr, comparisons, exchanges


def quicksort_median_pivot(arr, low, high, comparisons=0, exchanges=0):
    if low < high:
        pivot_index, comp, exch = partition_median(arr, low, high)
        comparisons += comp
        exchanges += exch
        arr, comp, exch = quicksort_median_pivot(arr, low, pivot_index - 1, comparisons, exchanges)
        comparisons += comp
        exchanges += exch
        arr, comp, exch = quicksort_median_pivot(arr, pivot_index + 1, high, comparisons, exchanges)
        comparisons += comp
        exchanges += exch
    return arr, comparisons, exchanges


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


def natural_merge_sort(head, comparisons=0, exchanges=0):
    if head is None or head.next is None:
        return head, comparisons, exchanges

    left_half, right_half = split_list(head)
    left_sorted, left_comp, left_exch = natural_merge_sort(left_half)
    right_sorted, right_comp, right_exch = natural_merge_sort(right_half)

    merged, merge_comp, merge_exch = merge_sorted_lists(left_sorted, right_sorted)
    total_comp = left_comp + right_comp + merge_comp
    total_exch = left_exch + right_exch + merge_exch

    return merged, total_comp, total_exch


def split_list(head):
    # Split the linked list into two halves
    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    middle = slow.next
    slow.next = None
    return head, middle


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
