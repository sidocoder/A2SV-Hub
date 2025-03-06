# Problem: Longest Contiguous Subarray With Absolute Diff Less Than or Equal to Limit - https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        _max = deque()
        _min = deque()
        max_length = 0

        left = 0
        for right in range(len(nums)):
            while _max and nums[right] > _max[-1]:
                _max.pop()
            _max.append(nums[right])
            while _min and nums[right] < _min[-1]:
                _min.pop()
            _min.append(nums[right])
        
            while _max[0] - _min[0] > limit:
                if _max[0] == nums[left]:
                    _max.popleft()
                if _min[0] == nums[left]:
                    _min.popleft()
                left += 1

            max_length = max(max_length, right - left + 1)

        return max_length

