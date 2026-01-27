class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        
        if len(s) < k:
            return reversed(s)
        
        else:
            i = 0
            j = k
            s = s.split()
            while i <= j:
                s[i], s[j-1] = s[j-1], s[i]
                i += 1
                j -= 1
        return "".join(s)