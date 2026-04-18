"""
Searching Algorithms.
Binary search variants, and search in special arrays.

| Algorithm               | Time    | Space |
|-------------------------|---------|-------|
| Binary search           | O(log n)| O(1)  |
| Search in rotated array | O(log n)| O(1)  |
| Search matrix           | O(log(m*n))| O(1)|
"""
from typing import List, Optional


def binary_search(arr: List[int], target: int) -> int:
    """
    Standard binary search on a sorted array.
    Returns index of target, or -1 if not found. O(log n).
    """
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1


def binary_search_leftmost(arr: List[int], target: int) -> int:
    """
    Returns the leftmost (first) index of target.
    Returns -1 if not found. O(log n).
    """
    lo, hi, result = 0, len(arr) - 1, -1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            result = mid
            hi = mid - 1
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return result


def binary_search_rotated(arr: List[int], target: int) -> int:
    """
    Binary search in a rotated sorted array with no duplicates.
    Returns index or -1. O(log n).
    Example: [4,5,6,7,0,1,2], target=0 → 4
    """
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid
        # Left half is sorted
        if arr[lo] <= arr[mid]:
            if arr[lo] <= target < arr[mid]:
                hi = mid - 1
            else:
                lo = mid + 1
        # Right half is sorted
        else:
            if arr[mid] < target <= arr[hi]:
                lo = mid + 1
            else:
                hi = mid - 1
    return -1


def search_2d_matrix(matrix: List[List[int]], target: int) -> bool:
    """
    Search in a sorted m×n matrix where each row is sorted
    and the first element of each row > last of previous row.
    O(log(m * n)).
    """
    if not matrix or not matrix[0]:
        return False
    m, n = len(matrix), len(matrix[0])
    lo, hi = 0, m * n - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        val = matrix[mid // n][mid % n]
        if val == target:
            return True
        elif val < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return False


def find_peak_element(arr: List[int]) -> int:
    """
    Find any peak element (greater than neighbours).
    Returns index. O(log n).
    """
    lo, hi = 0, len(arr) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if arr[mid] < arr[mid + 1]:
            lo = mid + 1
        else:
            hi = mid
    return lo


def find_minimum_rotated(arr: List[int]) -> int:
    """
    Find minimum in a rotated sorted array. O(log n).
    """
    lo, hi = 0, len(arr) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if arr[mid] > arr[hi]:
            lo = mid + 1
        else:
            hi = mid
    return arr[lo]
