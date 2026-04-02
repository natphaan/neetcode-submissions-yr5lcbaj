# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # brute force: turn into array and iterate through, with having i == n to stop the loop

        # nodes = []
        # curr = head

        # while curr:
        #     nodes.append(curr)
        #     curr = curr.next

        # removeIndex = len(nodes) - n

        # # edge case where if there is only head
        # if removeIndex == 0:
        #     return head.next # basically null

        # nodes[removeIndex - 1].next = nodes[removeIndex].next
        # return head


        # optimized

        dummy = ListNode(0, head) # want .next to be head
        l = dummy
        r = head # start at head for now


        # move r pointer to cover n distance from l
        while n > 0 and r:
            r = r.next
            n -= 1
    
        # now move r pointer to end of list
        while r:
            l = l.next
            r = r.next
        
        # at this point l is sitting just before the node we want to remove
        l.next = l.next.next

        return dummy.next


        
        


        