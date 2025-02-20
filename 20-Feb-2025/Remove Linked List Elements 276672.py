# Problem: Remove Linked List Elements - https://leetcode.com/problems/remove-linked-list-elements/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        prev = dummy
        itr = prev.next

        while itr:
            if itr.val == val:
                prev.next = itr.next
                itr= prev.next
            else:
                prev = prev.next
                itr = itr.next
        return dummy.next
