class ListNode:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node


class LinkedList:
    
    def __init__(self):
        # dummy node
        self.head = ListNode(-1) # default to value -1
        self.tail = self.head

    
    def get(self, index: int) -> int:

        # since we are on the dummy node, lets move it to next
        current = self.head.next
        # want a counter 
        i = 0
        while current:
            if i == index: # 
                return current.val
            i +=1
            current = current.next
        return -1 # since the index is out of bounds or list is empty

        

    def insertHead(self, val: int) -> None:
        newNode = ListNode(val) # make a node with the new val
        newNode.next = self.head.next
        self.head.next = newNode

        # if list is empty
        if not newNode.next:
            self.tail = newNode


    
        

    def insertTail(self, val: int) -> None:

        newNode = ListNode(val)
        self.tail.next = newNode
        self.tail = newNode
        



        

    def remove(self, index: int) -> bool:
        
        curr = self.head # should be at dummy node?
        i = 0
        
        # we want to remove the node --> my mistake was removing it at that elem
        # should be noted that it is better to remove the node just before

        while curr and i < index:
            i += 1
            curr = curr.next

        # we should be at the 1 away from the target node to remove
        # check if the index is valid when removing

        if curr and curr.next:
            if curr.next == self.tail: # if the next node is the tail
                self.tail = curr
            curr.next = curr.next.next
            return True
        return False

        
        




        

    def getValues(self) -> List[int]:
        curr = self.head.next
        res = []
        while curr:
            res.append(curr.val)
            # had this but then kept getting memory error so looked at solution
            # forgot to increment the next pointer
            curr = curr.next
        return res

        
