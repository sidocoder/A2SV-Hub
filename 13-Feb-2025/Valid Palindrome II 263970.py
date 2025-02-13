# Problem: Valid Palindrome II - https://leetcode.com/problems/valid-palindrome-ii/description/

class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palindrome(sub):
            return sub == sub[::-1]
    
        left, right = 0, len(s) - 1
    
        while left < right:
            if s[left] != s[right]:
                return is_palindrome(s[left+1:right+1]) or is_palindrome(s[left:right])
            left += 1
            right -= 1
    
        return True
