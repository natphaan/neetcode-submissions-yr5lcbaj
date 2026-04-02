# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        # whats stumping me are the 0, .., 1, .., 2
        # read and write pointers?

        # from solution:
        # want to find the middle of limked list w slow and fast pointers
        # 

        slow = head
        fast = head.next

        # this block of code finds the middle of list

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next # we need to grab head of second half of linekd list 
        prev = None # helps prep the second half reversal
        slow.next = None # literal act of cutting list in half


        # second while loop reverses the second half of list 
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp



        first, second = head, prev

        while second:
            tmp1 = first.next
            tmp2 = second.next
            first.next = second
            second.next = tmp1

            # update the pointers
            first = tmp1
            second = tmp2

        

        

        
        