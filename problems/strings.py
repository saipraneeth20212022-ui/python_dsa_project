"""
String Problems — LeetCode style.
"""
from typing import List
from collections import defaultdict


def is_valid_parentheses(s: str) -> bool:
    """
    Valid parentheses: (), [], {}.
    Approach: Stack.
    Time: O(n)  Space: O(n)
    """
    stack: List[str] = []
    pairs = {')': '(', ']': '[', '}': '{'}
    for ch in s:
        if ch in pairs:
            if not stack or stack[-1] != pairs[ch]:
                return False
            stack.pop()
        else:
            stack.append(ch)
    return not stack


def longest_palindromic_substring(s: str) -> str:
    """
    Find longest palindromic substring.
    Approach: Expand around centre for each index.
    Time: O(n²)  Space: O(1)
    """
    def expand(l: int, r: int) -> str:
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1; r += 1
        return s[l + 1: r]

    best = ""
    for i in range(len(s)):
        for candidate in (expand(i, i), expand(i, i + 1)):
            if len(candidate) > len(best):
                best = candidate
    return best


def group_anagrams(words: List[str]) -> List[List[str]]:
    """
    Group words that are anagrams of each other.
    Approach: Sort each word as a key.
    Time: O(n * m log m)  Space: O(n * m)
    """
    groups: dict = defaultdict(list)
    for word in words:
        groups[tuple(sorted(word))].append(word)
    return list(groups.values())


def encode_decode(strs: List[str]) -> List[str]:
    """
    Encode a list of strings, then decode back.
    Approach: Length-prefix encoding.
    Time: O(n)  Space: O(n)
    """
    encoded = "".join(f"{len(s)}#{s}" for s in strs)
    decoded: List[str] = []
    i = 0
    while i < len(encoded):
        j = encoded.index("#", i)
        length = int(encoded[i:j])
        decoded.append(encoded[j + 1: j + 1 + length])
        i = j + 1 + length
    return decoded


def is_palindrome(s: str) -> bool:
    """
    Check if a string (ignoring non-alphanumerics, case-insensitive) is a palindrome.
    Time: O(n)  Space: O(1)
    """
    cleaned = [c.lower() for c in s if c.isalnum()]
    return cleaned == cleaned[::-1]


def roman_to_int(s: str) -> int:
    """
    Convert Roman numeral string to integer.
    Time: O(n)  Space: O(1)
    """
    val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    for i in range(len(s)):
        if i + 1 < len(s) and val[s[i]] < val[s[i + 1]]:
            result -= val[s[i]]
        else:
            result += val[s[i]]
    return result


if __name__ == "__main__":
    print("is_valid_parentheses('()[]{}'): ", is_valid_parentheses("()[]{}"))
    print("longest_palindromic_substring('babad'):", longest_palindromic_substring("babad"))
    print("group_anagrams(['eat','tea','tan','ate','nat','bat']):")
    for g in group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]):
        print("  ", g)
    print("roman_to_int('MCMXCIV'):", roman_to_int("MCMXCIV"))
