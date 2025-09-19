class Solution:
    def minParentheses(self, s):
        # code here
        open_needed = 0  # Count of unmatched '('
        insertions = 0   # Total insertions needed

        for ch in s:
            if ch == '(':
                open_needed += 1
            elif ch == ')':
                if open_needed > 0:
                    open_needed -= 1  # Match with a previous '('
                else:
                    insertions += 1  # Need to insert a '(' before this ')'

        # Any remaining unmatched '(' need a ')' to balance
        return insertions + open_needed