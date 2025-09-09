class Solution:
    def assignHole(self, mices, holes):
        # code here
        mices.sort()

        holes.sort()

        m=0

        for i in range(len(mices)):

            r=abs(mices[i]-holes[i]) 

            m=max(m,r)

        return m