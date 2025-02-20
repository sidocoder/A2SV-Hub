# Problem: Remove Duplicates from Sorted List - https://leetcode.com/problems/remove-duplicates-from-sorted-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        seen = set()
        seen.add(head.val)
        current = head

        while current.next:
            if current.next.val in seen:  
                current.next = current.next.next 
            else:
                seen.add(current.next.val)
                current = current.next
        return head


        