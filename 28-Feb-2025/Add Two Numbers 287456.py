# Problem: Add Two Numbers - https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize the dummy node and current pointer
        dummy = ListNode()
        current = dummy
        carry = 0
        
        # Traverse both lists until both are exhausted
        while l1 or l2 or carry:
            # Get the values from l1 and l2 if available
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Calculate the new sum and carry
            total = val1 + val2 + carry
            carry = total // 10
            new_val = total % 10
            
            # Create a new node with the calculated value
            current.next = ListNode(new_val)
            current = current.next
            
            # Move to the next nodes in l1 and l2 if available
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
                
        # Return the head of the new list
        return dummy.next
