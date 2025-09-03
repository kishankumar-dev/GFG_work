"""
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None
"""

class Solution:
    def reverse(self, head):
        # code here
        prev=None
        temp=head
        while temp:
            curr=temp.next
            temp.next=prev
            prev=temp
            temp=curr
        return prev  
        