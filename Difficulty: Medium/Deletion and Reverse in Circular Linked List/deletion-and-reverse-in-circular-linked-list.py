#User function Template for python3
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''
class Solution:
    def reverse(self, head):
        if not head or not head.next:
            return head
        
        prev = None
        current = head
        next_node = current.next
        
        while True:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
            
            if current == head:  
                break
        
        
        head.next = prev
        return prev  
    
    def deleteNode(self, head, key):
        if not head:
            return None
        
        current = head
        
        if head.data == key:
            
            temp = head
            while temp.next != head:
                temp = temp.next
            if head == temp:  
                return None  
            temp.next = head.next 
            return head.next  
        
      
        while current.next != head:
            if current.next.data == key:
                current.next = current.next.next
                return head
            current = current.next
        
        return head 

#{ 
 # Driver Code Starts
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


def printList(head):
    if head is None:
        print("empty")
        return

    temp = head
    while True:
        print(temp.data, end=" ")
        temp = temp.next
        if temp == head:
            break
    print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        key = int(input())

        head = Node(arr[0])
        tail = head
        for i in range(1, len(arr)):
            tail.next = Node(arr[i])
            tail = tail.next
        tail.next = head  # Make the list circular

        ob = Solution()
        head = ob.deleteNode(head, key)
        head = ob.reverse(head)
        printList(head)

# } Driver Code Ends