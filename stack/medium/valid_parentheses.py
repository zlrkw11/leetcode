class Solution:
    def isValid(self, s: str) -> bool:
        
        stk = []
        d = {')':'(', ']':'[', '}':
        '{'}

        for c in s:
            if c in d and stk:
                if d[c] != stk[-1]:
                    return False
                else:
                    stk.pop()
            else:
                stk.append(c)
        return not stk
       