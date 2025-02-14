# Problem: Replace the Substring for Balanced String - https://leetcode.com/problems/replace-the-substring-for-balanced-string/

class Solution:
    def balancedString(self, s: str) -> int:
        n=len(s)
        div=n//4
        counter_s=Counter(s)
        new={}
        for cnt,val in counter_s.items():
            if val>div:
                new[cnt]=val-div
        if len(new)==0:
            return 0
        left = 0
        minimum = float("inf")
        start, end = 0, 0
        required = len(new)
        formed = 0
        curr_counter=Counter()
        for right in range(len(s)):
            char = s[right]
            curr_counter[char] += 1
            
            if char in new and curr_counter[char] == new[char]:
                formed += 1
            
            while left <= right and formed == required:
                if right - left < minimum:
                    minimum = right - left
                    start, end = left, right
                
                left_char = s[left]
                curr_counter[left_char] -= 1
                
                if left_char in new and curr_counter[left_char] < new[left_char]:
                    formed -= 1
                
                left += 1  
        
        return end-start+1
