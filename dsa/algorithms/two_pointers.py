"""
Two Pointers Technique.
Common patterns: opposite ends, same direction, fast/slow.
"""
from typing import List, Optional, Tuple


def two_sum_sorted(arr: List[int], target: int) -> Optional[Tuple[int, int]]:
    """
    Two Sum on sorted array. O(n) time, O(1) space.
    Returns (index1, index2) or None.
    """
    lo, hi = 0, len(arr) - 1
    while lo < hi:
        s = arr[lo] + arr[hi]
        if s == target:
            return lo, hi
        elif s < target:
            lo += 1
        else:
            hi -= 1
    return None


def three_sum(arr: List[int]) -> List[Tuple[int, int, int]]:
    """
    Find all unique triplets summing to zero. O(n²).
    """
    arr.sort()
    result: List[Tuple[int, int, int]] = []
    for i in range(len(arr) - 2):
        if i > 0 and arr[i] == arr[i - 1]:
            continue
        lo, hi = i + 1, len(arr) - 1
        while lo < hi:
            s = arr[i] + arr[lo] + arr[hi]
            if s == 0:
                result.append((arr[i], arr[lo], arr[hi]))
                while lo < hi and arr[lo] == arr[lo + 1]:
                    lo += 1
                while lo < hi and arr[hi] == arr[hi - 1]:
                    hi -= 1
                lo += 1; hi -= 1
            elif s < 0:
                lo += 1
            else:
                hi -= 1
    return result


def container_with_most_water(heights: List[int]) -> int:
    """
    Largest rectangle between two vertical lines. O(n).
    """
    lo, hi, max_water = 0, len(heights) - 1, 0
    while lo < hi:
        water = min(heights[lo], heights[hi]) * (hi - lo)
        max_water = max(max_water, water)
        if heights[lo] < heights[hi]:
            lo += 1
        else:
            hi -= 1
    return max_water


def remove_duplicates_sorted(arr: List[int]) -> int:
    """
    Remove duplicates from sorted array in-place. O(n).
    Returns the length of the deduplicated prefix.
    """
    if not arr:
        return 0
    write = 1
    for read in range(1, len(arr)):
        if arr[read] != arr[read - 1]:
            arr[write] = arr[read]
            write += 1
    return write


def sort_colors(arr: List[int]) -> None:
    """
    Dutch National Flag — sort [0,1,2] in-place. O(n), one pass.
    """
    lo = mid = 0
    hi = len(arr) - 1
    while mid <= hi:
        if arr[mid] == 0:
            arr[lo], arr[mid] = arr[mid], arr[lo]
            lo += 1; mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[mid], arr[hi] = arr[hi], arr[mid]
            hi -= 1
