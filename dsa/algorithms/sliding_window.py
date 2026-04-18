"""
Sliding Window Technique.
Fixed-size and variable-size windows.
"""
from collections import defaultdict
from typing import List, Optional, Tuple


def max_sum_subarray_fixed(arr: List[int], k: int) -> int:
    """
    Maximum sum subarray of exactly size k. O(n).
    """
    if len(arr) < k:
        raise ValueError("Array too short")
    window_sum = sum(arr[:k])
    max_sum = window_sum
    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i - k]
        max_sum = max(max_sum, window_sum)
    return max_sum


def longest_substring_no_repeat(s: str) -> int:
    """
    Longest substring without repeating characters. O(n).
    """
    seen: dict = {}
    left = max_len = 0
    for right, ch in enumerate(s):
        if ch in seen and seen[ch] >= left:
            left = seen[ch] + 1
        seen[ch] = right
        max_len = max(max_len, right - left + 1)
    return max_len


def min_window_substring(s: str, t: str) -> str:
    """
    Minimum window in s containing all characters of t. O(n).
    Returns empty string if no window found.
    """
    if not t or not s:
        return ""
    need = defaultdict(int)
    for ch in t:
        need[ch] += 1
    missing = len(t)
    best_start, best_len = 0, float("inf")
    left = 0
    for right, ch in enumerate(s):
        if need[ch] > 0:
            missing -= 1
        need[ch] -= 1
        if missing == 0:
            while need[s[left]] < 0:
                need[s[left]] += 1
                left += 1
            window_len = right - left + 1
            if window_len < best_len:
                best_len = window_len
                best_start = left
            need[s[left]] += 1
            missing += 1
            left += 1
    return s[best_start: best_start + int(best_len)] if best_len != float("inf") else ""


def longest_substring_with_k_distinct(s: str, k: int) -> int:
    """
    Longest substring with at most k distinct characters. O(n).
    """
    count: dict = defaultdict(int)
    left = max_len = 0
    for right, ch in enumerate(s):
        count[ch] += 1
        while len(count) > k:
            count[s[left]] -= 1
            if count[s[left]] == 0:
                del count[s[left]]
            left += 1
        max_len = max(max_len, right - left + 1)
    return max_len


def find_all_anagrams(s: str, p: str) -> List[int]:
    """
    Find all start indices of p's anagrams in s. O(n).
    """
    if len(p) > len(s):
        return []
    p_count: List[int] = [0] * 26
    w_count: List[int] = [0] * 26
    for ch in p:
        p_count[ord(ch) - ord('a')] += 1
    result: List[int] = []
    for i, ch in enumerate(s):
        w_count[ord(ch) - ord('a')] += 1
        if i >= len(p):
            w_count[ord(s[i - len(p)]) - ord('a')] -= 1
        if w_count == p_count:
            result.append(i - len(p) + 1)
    return result
