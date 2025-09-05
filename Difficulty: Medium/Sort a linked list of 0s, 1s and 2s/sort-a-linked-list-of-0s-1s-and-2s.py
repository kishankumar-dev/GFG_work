'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
	
class Solution:
    def segregate(self, head):
        #code here
        dummy_zero = zero = Node(0)
        dummy_one = one = Node(0)
        dummy_two = two = Node(0)
        
        while head:
            h = head
            head = head.next
            h.next = None
            match h.data:
                case 0:
                    zero.next = h
                    zero = zero.next
                case 1:
                    one.next = h
                    one = one.next
                case 2:
                    two.next = h
                    two = two.next
                case _:
                    raise ValueError("?")
        
        one.next = dummy_two.next
        zero.next = dummy_one.next
        
        return dummy_zero.next