class ListNode:

    def __init__(self, val, next_node=None, prev_node=None):

        self.val = val
        self.next = next_node
        self.prev = prev_node

class Deque:
    
    def __init__(self):

        self.head = ListNode(0)
        self.tail = ListNode(0)

        self.head.next = self.tail
        self.tail.prev = self.head

    def isEmpty(self) -> bool:

        if self.head.next == self.tail:
            return True
        else:
            return False
        
    def append(self, value: int) -> None:

        new_node = ListNode(value)
        
        temp = self.tail.prev
        temp.next = new_node
        self.tail.prev = new_node

        new_node.prev = temp
        new_node.next = self.tail
        

    def appendleft(self, value: int) -> None:
        
        new_node = ListNode(value)

        temp = self.head.next
        temp.prev = new_node
        self.head.next = new_node

        new_node.next = temp
        new_node.prev = self.head

    def pop(self) -> int:
        
        if not self.isEmpty():

            poped_node = self.tail.prev
            temp = poped_node.prev

            temp.next = self.tail
            self.tail.prev = temp
        
            return poped_node.val

        else:
            return -1

    def popleft(self) -> int:

        if not self.isEmpty():

            poped_node = self.head.next
            temp = poped_node.next

            temp.prev = self.head
            self.head.next = temp
        
            return poped_node.val

        else:
            return -1


        
