'''
class Node:
    def __init__(self, d):
        self.data=d
        self.next=None
        self.bottom=None
        
'''

class Solution:
    def flatten(self, root):
        # code here
        hp=[]
        idx=0
        cur=root
        while cur:
            hp.append((cur.data,idx,cur,))
            idx+=1
            cur=cur.next
        import heapq
        heapq.heapify(hp)
        _,idx,cur=heapq.heappop(hp)
        if cur.bottom:
            heapq.heappush(hp,(cur.bottom.data,idx,cur.bottom,))
        while hp:
            _,idx,node=heapq.heappop(hp)
            if node.bottom:
                heapq.heappush(hp,(node.bottom.data,idx,node.bottom))
            cur.bottom=node
            cur=cur.bottom
        return root