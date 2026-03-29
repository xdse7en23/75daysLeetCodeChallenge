class Solution(object):
    def isValid(self, s):
        stack = []
        
        for ch in s:
            if ch == '(' or ch == '{' or ch == '[':
                stack.append(ch)
            else:
                if not stack:
                    return False
                
                top = stack.pop()
                
                if ch == ')' and top != '(':
                    return False
                if ch == '}' and top != '{':
                    return False
                if ch == ']' and top != '[':
                    return False
        
        return len(stack) == 0