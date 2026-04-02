# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode()
        curr = dummy
        carry = 0

        while l1 or l2 or carry:
            if l1:
                v1 = l1.val # get the value and store it with v1
            else:
                v1 = 0 # otherwise if no l1
            if l2:
                v2 = l2.val # get value and store it with v2
            else:
                v2 = 0 # otherwise if no l2
            

            # new digit

            val = v1 + v2 + carry
            carry = val // 10
            val = val % 10
            curr.next = ListNode(val)


            # update the pointers

            curr = curr.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next

            



        