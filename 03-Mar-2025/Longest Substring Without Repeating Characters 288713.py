# Problem: Longest Substring Without Repeating Characters - https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        max_length = 0
        start = 0
        char_index_map = {}
        for end in range(len(s)):
            if s[end] in char_index_map:
                start = max(start, char_index_map[s[end]] + 1)
            char_index_map[s[end]] = end
            max_length = max(max_length, end - start + 1)
        return max_length