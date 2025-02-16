# Problem: 3 Sum Closest - https://leetcode.com/problems/3sum-closest/description/

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        closest = inf
        for i ,v in enumerate(nums):
            j,k = i+1,n-1
            while j<k:
                _sum = v +nums[j] +nums[k]
                if _sum > target:
                    k-=1
                else:
                    j+=1
                if abs(_sum -target) < abs(closest-target):
                    closest = _sum
      
        return closest