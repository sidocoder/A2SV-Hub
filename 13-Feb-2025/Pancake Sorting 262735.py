# Problem: Pancake Sorting - https://leetcode.com/problems/pancake-sorting/

class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        
        def flip(k):
            arr[:k] = arr[:k][::-1]  
        
        res = []
        n = len(arr)

        for size in range(n, 1, -1):
            max_index = arr.index(size) 

            if max_index == size - 1:
                continue  

            if max_index != 0:
                res.append(max_index + 1)  
                flip(max_index + 1)

            res.append(size)  
            flip(size)

        return res