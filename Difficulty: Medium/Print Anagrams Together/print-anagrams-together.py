class Solution:
    def anagrams(self, arr):
        '''
        words: list of words
        n:     number of words
        return: list of groups of anagrams
        '''
        res = []
        list_index = {}

        # Create a mapping of sorted word to their original indices
        for i in range(len(arr)):
            sorted_word = "".join(sorted(arr[i]))
            if sorted_word in list_index:
                list_index[sorted_word].append(arr[i])
            else:
                list_index[sorted_word] = [arr[i]]

        # Add all groups of anagrams to the result
        for group in list_index.values():
            res.append(group)

        return res

#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    t = int(input())
    for tcs in range(t):
        words = input().split()

        ob = Solution()
        ans = ob.anagrams(words)

        for grp in sorted(ans):
            for word in grp:
                print(word, end=' ')
            print()

        print("~")

# } Driver Code Ends