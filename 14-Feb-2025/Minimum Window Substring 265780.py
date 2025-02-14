# Problem: Minimum Window Substring - https://leetcode.com/problems/minimum-window-substring/submissions/

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m = len(s)
        n = len(t)
        if n > m:
            return ''
            
        count_t = Counter(t)
        required = len(count_t)  

        left, right = 0, 0
        window_count = {}
        formed = 0  
        min_length = float("inf")
        min_substr = ""

        while right < len(s):
            char = s[right]
            window_count[char] = window_count.get(char, 0) + 1

            if char in count_t and window_count[char] == count_t[char]:
                formed += 1

            while left <= right and formed == required:
                if right - left + 1 < min_length:
                    min_length = right - left + 1
                    min_substr = s[left:right+1]

            
                window_count[s[left]] -= 1
                if s[left] in count_t and window_count[s[left]] < count_t[s[left]]:
                    formed -= 1 
                left += 1

            right += 1  

        return min_substr

            




