# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # use a stack?? every time i remove a node, add it to stack
        # no its more about modifying the pointer right
        # from solution, two ways to traverse linked list
        # two pointers or recursion
        # going with two pointers 

        # define some nodes
        prev = None # for now
        curr = head # current pointer

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

        
        