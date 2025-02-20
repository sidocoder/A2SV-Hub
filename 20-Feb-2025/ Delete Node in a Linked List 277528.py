# Problem:  Delete Node in a Linked List - https://leetcode.com/problems/delete-node-in-a-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        node.val = node.next.val
        node.next  = node.next.next   
# prev = None
        # curr = node
        
        # while curr:
        #     if curr.val != node:
        #         curr = curr.next
        #         prev = curr
        #     else:
        #         prev.next = curr.next
        #         prev = curr.next
        #         curr = curr.next
        # return node


        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        