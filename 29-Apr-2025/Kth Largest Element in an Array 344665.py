# Problem: Kth Largest Element in an Array - https://leetcode.com/problems/kth-largest-element-in-an-array/description/

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        sorted_nums = sorted(nums, reverse=True)
        return sorted_nums[k -1]
        # def heapSort(self, arr):
        #     def swap(arr, i, j):
        #         arr[i],arr[j]=arr[j],arr[i]
        #         return arr
            
        #     def heapify_down(arr,n,curr):
        #         r_ch = 2*curr + 2
        #         l_ch = 2*curr + 1
        #         large = curr
                
        #         if l_ch < n and arr[large] > arr[l_ch]:
        #             large = l_ch
        #         if r_ch < n and arr[large] > arr[r_ch]:
        #             large = r_ch
                
        #         if large != curr:
        #             swap(arr,large,curr)
        #             heapify_down(arr,n,large)
        #         return arr
                
            
        #     n = len(arr)
        #     for i in range(n//2 -1,-1,-1):
        #         heapify_down(arr,n,i)
                
        #     for end in range(n-1,-1,-1):
        #         swap(arr,0,end)
        #         heapify_down(arr,end,0)
        # heapSort(self,nums)
        # return nums[k -1]
                






            