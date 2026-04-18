"""
Sorting Algorithms.
All functions return a new sorted list (non-mutating).

| Algorithm  | Best     | Average  | Worst    | Space  | Stable |
|------------|----------|----------|----------|--------|--------|
| Merge Sort | O(n log n)| O(n log n)| O(n log n)| O(n)  | Yes    |
| Quick Sort | O(n log n)| O(n log n)| O(n²)   | O(log n)| No    |
| Heap Sort  | O(n log n)| O(n log n)| O(n log n)| O(1)  | No     |
| Tim Sort   | O(n)      | O(n log n)| O(n log n)| O(n)  | Yes    |
| Counting   | O(n+k)    | O(n+k)   | O(n+k)   | O(k)   | Yes    |
"""
from typing import List


def merge_sort(arr: List[int]) -> List[int]:
    """Divide-and-conquer sort. O(n log n), O(n) space. Stable."""
    if len(arr) <= 1:
        return arr[:]
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return _merge(left, right)


def _merge(left: List[int], right: List[int]) -> List[int]:
    result, i, j = [], 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i]); i += 1
        else:
            result.append(right[j]); j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def quick_sort(arr: List[int]) -> List[int]:
    """Lomuto partition. O(n log n) average, O(n²) worst. O(log n) stack space."""
    if len(arr) <= 1:
        return arr[:]
    result = arr[:]
    _quick_sort_inplace(result, 0, len(result) - 1)
    return result


def _quick_sort_inplace(arr: List[int], low: int, high: int) -> None:
    if low < high:
        pivot_idx = _partition(arr, low, high)
        _quick_sort_inplace(arr, low, pivot_idx - 1)
        _quick_sort_inplace(arr, pivot_idx + 1, high)


def _partition(arr: List[int], low: int, high: int) -> int:
    # Median-of-three pivot for better performance
    mid = (low + high) // 2
    if arr[mid] < arr[low]:
        arr[low], arr[mid] = arr[mid], arr[low]
    if arr[high] < arr[low]:
        arr[low], arr[high] = arr[high], arr[low]
    if arr[mid] < arr[high]:
        arr[mid], arr[high] = arr[high], arr[mid]
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def heap_sort(arr: List[int]) -> List[int]:
    """Heap sort. O(n log n), O(1) space. Not stable."""
    result = arr[:]
    n = len(result)

    def sift_down(root: int, end: int) -> None:
        while True:
            largest, left, right = root, 2 * root + 1, 2 * root + 2
            if left < end and result[left] > result[largest]:
                largest = left
            if right < end and result[right] > result[largest]:
                largest = right
            if largest == root:
                break
            result[root], result[largest] = result[largest], result[root]
            root = largest

    for i in range(n // 2 - 1, -1, -1):
        sift_down(i, n)
    for end in range(n - 1, 0, -1):
        result[0], result[end] = result[end], result[0]
        sift_down(0, end)
    return result


def counting_sort(arr: List[int]) -> List[int]:
    """
    Counting sort for non-negative integers.
    O(n + k) time and space where k = max(arr).
    """
    if not arr:
        return []
    max_val = max(arr)
    count = [0] * (max_val + 1)
    for val in arr:
        count[val] += 1
    result = []
    for val, freq in enumerate(count):
        result.extend([val] * freq)
    return result
