# Problem: Partition List - https://leetcode.com/problems/partition-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        first = []
        second = []
        while head:
            if head.val >= x:
                second.append(head.val)
            else:
                first.append(head.val)
            head = head.next
        arr = first + second
        dumpy = ListNode()
        curr = dumpy
        for i in arr:
            curr.next = ListNode(i)
            curr = curr.next
        return dumpy.next



        