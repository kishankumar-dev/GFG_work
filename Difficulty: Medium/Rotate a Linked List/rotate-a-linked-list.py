# Your task is to complete this function

'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''

class Solution:
    #Function to rotate a linked list.
    def rotate(self, head, k):
        temp=head
        li=[]
        while temp is not None:
            li.append(temp.data)
            temp=temp.next
        li1=[]
        for i in range(k,len(li)):
            li1.append(li[i])
        li1.extend(li)
        new_k=len(li)
        new_list=Node(li1[0])
        head1=new_list
        j=0
        while j<new_k:
            new_list.next=Node(li1[j])
            new_list=new_list.next
            j+=1
        return head1.next

#{ 
 # Driver Code Starts
#Initial Template for Python 3


# Define the Node class for the linked list
class Node:

    def __init__(self, x):
        self.data = x
        self.next = None


# Function to print the linked list
def printList(node):
    while node:
        print(node.data, end=" ")
        node = node.next
    print()


#Position this line where user code will be pasted.

# Main function
if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().splitlines()

    t = int(data[0].strip())
    idx = 1

    while t > 0:
        arr = list(map(int, data[idx].strip().split()))

        head = None
        if arr:
            head = Node(arr[0])
            tail = head
            for num in arr[1:]:
                tail.next = Node(num)
                tail = tail.next

        k = int(data[idx + 1].strip())
        idx += 2
        head = Solution().rotate(head, k)
        printList(head)
        t -= 1

# } Driver Code Ends