# Problem: Merge k Sorted Lists - https://leetcode.com/problems/merge-k-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # for i in range(len(lists)):
        heap = []
        
        for i, node in enumerate(lists):
            if node:
                heappush(heap, (node.val,i, node))

        dummy = ListNode(0)
        curr = dummy
        while heap:
            val,ind,node = heappop(heap)
            curr.next = node
            curr = curr.next
            if node.next:
                heappush(heap, (node.next.val,ind, node.next))
        return dummy.next



        