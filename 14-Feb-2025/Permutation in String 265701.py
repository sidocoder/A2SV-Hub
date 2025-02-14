# Problem: Permutation in String - https://leetcode.com/problems/permutation-in-string/

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
              
        k = len(s1)
        count_s1 = Counter(s1)
        window_count = Counter(s2[:k])
        def check(first,second):
            for char in first:
                if second[char] != first[char]:
                    return False
            return True

        
        left = 0
        for right in range(k ,len(s2)):
            if check(count_s1, window_count):
                return True
            window_count[s2[left]] -= 1
            window_count[s2[right]] += 1
            left += 1

        if check(count_s1,window_count):
            return True
        return False
            # window_count.add(s1[right])

           
                

            

