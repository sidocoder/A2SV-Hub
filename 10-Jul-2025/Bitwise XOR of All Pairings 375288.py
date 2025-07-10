# Problem: Bitwise XOR of All Pairings - https://leetcode.com/problems/bitwise-xor-of-all-pairings/description/?envType=problem-list-v2&envId=brainteaser

class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        # nums1len = len(nums1)
        # nums2len = len(nums2)
        # nums3 = []

        # for i in range(nums1len):
        #     for j in range(nums2len):
        #         nums3.append(nums1[i] ^ nums2[j])

        # xor = 0
        # for i in range(len(nums3)):
        #     xor ^= nums3[i]
        # return xor
        xor1 = 0
        for num in nums1:
            xor1 ^= num

        xor2 = 0
        for num in nums2:
            xor2 ^= num

        if len(nums2) % 2 == 1:
            xor_result = xor1
        else:
            xor_result = 0

        if len(nums1) % 2 == 1:
            xor_result ^= xor2

        return xor_result
                
        