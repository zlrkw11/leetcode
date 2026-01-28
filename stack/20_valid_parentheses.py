class Solution:
    def isValid(self, s: str) -> bool:
        d = {")":"(", "]":"[","}":"{",}
        stk = []
        for i in range(len(s)):
            if s[i] in d.values():
                stk.append(s[i])
            else:
                if not stk:
                    return False
                elif stk[-1] != d[s[i]]:
                    return False
                else:
                    stk.pop()

        return not stk