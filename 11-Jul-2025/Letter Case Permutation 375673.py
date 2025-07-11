# Problem: Letter Case Permutation - https://leetcode.com/problems/letter-case-permutation/

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        result = [""]

        for char in s:
            if char.isalpha():
                temp = []
                for item in result:
                    temp.append(item + char.lower())
                    temp.append(item + char.upper())
                result = temp
            else:
                result = [item + char for item in result]

        return result
