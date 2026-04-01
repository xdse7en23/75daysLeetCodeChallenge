class Solution(object):
    def evalRPN(self, tokens):
        stack = []
        
        for t in tokens:
            if t == '+':
                stack.append(stack.pop() + stack.pop())
            
            elif t == '-':
                b = stack.pop()
                a = stack.pop()
                stack.append(a - b)
            
            elif t == '*':
                stack.append(stack.pop() * stack.pop())
            
            elif t == '/':
                b = stack.pop()
                a = stack.pop()
                stack.append(int(float(a) / b))  # ✅ FIX
            
            else:
                stack.append(int(t))
        
        return stack[0]