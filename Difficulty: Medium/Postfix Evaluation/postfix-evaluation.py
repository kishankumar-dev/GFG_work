class Solution:
    def evaluatePostfix(self, arr):
        # code here
        stack = []
        
        for token in arr:
            if token not in ["+", "-", "*", "/", "^"]:
                stack.append(int(token))
            else:
                b = stack.pop()
                a = stack.pop()
                
                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "*":
                    stack.append(a * b)
                elif token == "/":
                    stack.append(a // b)   # FIXED
                elif token == "^":
                    stack.append(a ** b)
        
        return stack[-1]