"""
Array Problems — LeetCode style.
Each problem includes: description, approach, time/space complexity.
"""
from typing import List, Optional, Dict


# ─────────────────────────────────────────────
# Problem 1: Two Sum
# ─────────────────────────────────────────────
def two_sum(nums: List[int], target: int) -> List[int]:
    """
    Find two indices such that nums[i] + nums[j] == target.
    Approach: Hash map for O(1) lookups.
    Time: O(n)  Space: O(n)
    """
    seen: Dict[int, int] = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []


# ─────────────────────────────────────────────
# Problem 2: Product of Array Except Self
# ─────────────────────────────────────────────
def product_except_self(nums: List[int]) -> List[int]:
    """
    Return array where output[i] = product of all elements except nums[i].
    No division allowed.
    Approach: Prefix products then suffix products.
    Time: O(n)  Space: O(1) (output array not counted)
    """
    n = len(nums)
    result = [1] * n
    prefix = 1
    for i in range(n):
        result[i] = prefix
        prefix *= nums[i]
    suffix = 1
    for i in range(n - 1, -1, -1):
        result[i] *= suffix
        suffix *= nums[i]
    return result


# ─────────────────────────────────────────────
# Problem 3: Best Time to Buy and Sell Stock
# ─────────────────────────────────────────────
def max_profit(prices: List[int]) -> int:
    """
    Find max profit from one buy-sell transaction.
    Approach: Track minimum price seen so far.
    Time: O(n)  Space: O(1)
    """
    min_price = float("inf")
    max_profit_val = 0
    for price in prices:
        min_price = min(min_price, price)
        max_profit_val = max(max_profit_val, price - min_price)
    return max_profit_val


# ─────────────────────────────────────────────
# Problem 4: Rotate Array
# ─────────────────────────────────────────────
def rotate(nums: List[int], k: int) -> None:
    """
    Rotate array right by k steps in-place.
    Approach: Three reverses.
    Time: O(n)  Space: O(1)
    """
    n = len(nums)
    k %= n

    def reverse(l: int, r: int) -> None:
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1; r -= 1

    reverse(0, n - 1)
    reverse(0, k - 1)
    reverse(k, n - 1)


# ─────────────────────────────────────────────
# Problem 5: Find Duplicate Number
# ─────────────────────────────────────────────
def find_duplicate(nums: List[int]) -> int:
    """
    Find the duplicate in array of n+1 ints in [1, n].
    Approach: Floyd's cycle detection (no extra space, no mutation).
    Time: O(n)  Space: O(1)
    """
    slow = fast = nums[0]
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break
    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
    return slow


# ─────────────────────────────────────────────
# Problem 6: Merge Intervals
# ─────────────────────────────────────────────
def merge_intervals(intervals: List[List[int]]) -> List[List[int]]:
    """
    Merge overlapping intervals.
    Approach: Sort by start, then greedily merge.
    Time: O(n log n)  Space: O(n)
    """
    if not intervals:
        return []
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    for start, end in intervals[1:]:
        if start <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])
    return merged


if __name__ == "__main__":
    print("two_sum([2,7,11,15], 9)        →", two_sum([2, 7, 11, 15], 9))
    print("product_except_self([1,2,3,4]) →", product_except_self([1, 2, 3, 4]))
    print("max_profit([7,1,5,3,6,4])      →", max_profit([7, 1, 5, 3, 6, 4]))
    print("find_duplicate([1,3,4,2,2])    →", find_duplicate([1, 3, 4, 2, 2]))
    print("merge_intervals([[1,3],[2,6]]) →", merge_intervals([[1, 3], [2, 6], [8, 10]]))
