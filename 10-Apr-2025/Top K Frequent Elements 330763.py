# Problem: Top K Frequent Elements - https://leetcode.com/problems/top-k-frequent-elements/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashh = Counter(nums)
        sorted_items = sorted(hashh.items(), key=lambda x: x[1], reverse=True)

        result = []
        count = 0
        for item in sorted_items:
            result.append(item[0])
            count += 1
            if count == k:
                break

        return result


        