"""
Dynamic Programming Algorithms.
Classic DP problems with bottom-up tabulation.
"""
from typing import List, Tuple


def fibonacci(n: int) -> int:
    """
    nth Fibonacci number using DP. O(n) time, O(1) space.
    """
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def knapsack(weights: List[int], values: List[int], capacity: int) -> int:
    """
    0/1 Knapsack problem. O(n * capacity) time and space.
    Returns the maximum value achievable within the weight capacity.
    """
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            dp[i][w] = dp[i - 1][w]
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
    return dp[n][capacity]


def longest_common_subsequence(s1: str, s2: str) -> int:
    """
    LCS length of two strings. O(m * n) time and space.
    """
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[m][n]


def longest_increasing_subsequence(arr: List[int]) -> int:
    """
    LIS length. O(n log n) using patience sorting with binary search.
    """
    import bisect
    tails: List[int] = []
    for val in arr:
        pos = bisect.bisect_left(tails, val)
        if pos == len(tails):
            tails.append(val)
        else:
            tails[pos] = val
    return len(tails)


def coin_change(coins: List[int], amount: int) -> int:
    """
    Minimum coins to make amount. O(amount * len(coins)) time.
    Returns -1 if impossible.
    """
    dp = [float("inf")] * (amount + 1)
    dp[0] = 0
    for coin in coins:
        for a in range(coin, amount + 1):
            dp[a] = min(dp[a], dp[a - coin] + 1)
    return int(dp[amount]) if dp[amount] != float("inf") else -1


def max_subarray(arr: List[int]) -> Tuple[int, int, int]:
    """
    Kadane's algorithm. O(n). Returns (max_sum, start_idx, end_idx).
    """
    max_sum = cur_sum = arr[0]
    start = end = temp_start = 0
    for i in range(1, len(arr)):
        if cur_sum + arr[i] < arr[i]:
            cur_sum = arr[i]
            temp_start = i
        else:
            cur_sum += arr[i]
        if cur_sum > max_sum:
            max_sum = cur_sum
            start = temp_start
            end = i
    return max_sum, start, end


def edit_distance(s1: str, s2: str) -> int:
    """
    Levenshtein edit distance. O(m * n) time and space.
    """
    m, n = len(s1), len(s2)
    dp = list(range(n + 1))
    for i in range(1, m + 1):
        prev = dp[0]
        dp[0] = i
        for j in range(1, n + 1):
            temp = dp[j]
            if s1[i - 1] == s2[j - 1]:
                dp[j] = prev
            else:
                dp[j] = 1 + min(prev, dp[j], dp[j - 1])
            prev = temp
    return dp[n]


def unique_paths(m: int, n: int) -> int:
    """
    Count unique paths in m×n grid, top-left to bottom-right.
    O(m * n) time, O(n) space.
    """
    dp = [1] * n
    for _ in range(1, m):
        for j in range(1, n):
            dp[j] += dp[j - 1]
    return dp[-1]
