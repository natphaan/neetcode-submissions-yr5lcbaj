# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        # how do we store which nodes have been visited?
        # hashmap? or set since if node 2 is visited and then goes back


        # seen = set()
        # curr = head

        # while curr:
        #     if curr in seen:
        #         return True
        #     seen.add(curr)
        #     curr = curr.next
        # return False


        # FAST AND SLOW POINTER WAY

        fast, slow = head, head

        while fast and fast.next: # why do we need fast.next?
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False



        