#User function Template for python3


class Solution:
    
    #Function to rotate matrix anticlockwise by 90 degrees.
    def rotateby90(self, mat): 
        # code here
        n=len(mat)
        i=0
        j=0
        while i<n and j<n:
            k=i+1
            while k<n:
                mat[k][j], mat[j][k] = mat[j][k], mat[k][j]
                k+=1
            i+=1
            j+=1
        mat.reverse()
        return mat

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    import sys
    input = sys.stdin.read
    data = input().split()

    t = int(data[0])
    index = 1

    for _ in range(t):
        n = int(data[index])
        index += 1
        matrix = []
        for i in range(n):
            row = list(map(int, data[index:index + n]))
            matrix.append(row)
            index += n
        obj = Solution()
        obj.rotateby90(matrix)
        for i in range(n):
            for j in range(n):
                print(matrix[i][j], end=" ")
            print()

        print("~")

# } Driver Code Ends