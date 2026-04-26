class Solution:
    def commonElements(self, a, b, c):
        # code here
        common = []
        ids = [0] * 3
        arrs = [a, b, c]
        end_not_reached = True
        while end_not_reached:
            if all(arrs[i][ids[i]] == arrs[i + 1][ids[i + 1]]  for i in range(2)):
                if not common or common[-1] != arrs[0][ids[0]]:
                    common.append(arrs[0][ids[0]])
                for i in range(3):
                    ids[i] += 1
                    if ids[i] == len(arrs[i]):
                        end_not_reached = False
            else:
                _, i = min((arrs[i][ids[i]], i) for i in range(3))
                ids[i] += 1
                if ids[i] == len(arrs[i]):
                    end_not_reached = False
        return common