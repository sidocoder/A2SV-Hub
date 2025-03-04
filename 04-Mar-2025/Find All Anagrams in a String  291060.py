# Problem: Find All Anagrams in a String  - https://leetcode.com/problems/find-all-anagrams-in-a-string/

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        
        p_count = Counter(p)      
        substring_count = Counter( s[:len(p)])
        left = 0
        ans = []
        for right in range(len(p), len(s)):                    
            if substring_count == p_count:
                ans.append(left)
            
            substring_count[s[left]] -= 1
            substring_count[s[right]] += 1
            # if substring_count[s[left]] == 0:
            #     del substring_count[s[left]] 
            left +=1
        if substring_count == p_count:
            ans.append(left)        

        return ans











        

        # p_count = Counter(p)
        # s_count = Counter(s[:len(p) - 1])
        # result = []

        # left = 0
        # for right in range(len(p) - 1, len(s)):
        #     s_count[s[right]] += 1 

        #     if s_count == p_count:  
        #         result.append(left)

        #     s_count[s[left]] -= 1  
        #     if s_count[s[left]] == 0:
        #         del s_count[s[left]]  

        #     left += 1  

        # return result
