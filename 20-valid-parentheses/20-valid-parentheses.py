class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        m = {
            '(' : ')',
            '[' : ']',
            '{' : '}'
        }

        for i in s:
            if len(stack) == 0:
                stack.append(i)
            elif stack[-1] in m.keys() and m[stack[-1]] == i:
                stack.pop()
            else:
                stack.append(i)
        
        return len(stack) == 0
            
