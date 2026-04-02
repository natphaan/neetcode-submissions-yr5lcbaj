"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        # seems like the hardest part is getting the random_index

        # sol: two passes --> one to put 

        curr = head
        
        copied = {None: None} # use a hashmap to store the node's values


        # using the original nodes as key and the copied nodes as value
        while curr:
            copy = Node(curr.val) # get the current Node info
            copied[curr] = copy # add it to hashmap
            curr = curr.next # increment
        

        # now we do a second pass
        curr = head

        while curr:
            copy = copied[curr]
            copy.next = copied[curr.next]
            copy.random = copied[curr.random]
            curr = curr.next
        
        return copied[head]


        
        