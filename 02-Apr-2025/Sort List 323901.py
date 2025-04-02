# Problem: Sort List - https://leetcode.com/problems/sort-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        def find_middle(node):
            slow = node
            fast = node.next

            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next

            return slow

        def merge(left, right):
            dummy = ListNode()
            current = dummy

            while left and right:
                if left.val < right.val:
                    current.next = left
                    left = left.next
                else:
                    current.next = right
                    right = right.next
                current = current.next

            current.next = left or right

            return dummy.next

        mid = find_middle(head)
        left = head
        right = mid.next
        mid.next = None

        sorted_left = self.sortList(left)
        sorted_right = self.sortList(right)

        return merge(sorted_left, sorted_right)