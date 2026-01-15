class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d = {}
        for l in magazine:
            if l not in d:
                d[l] = 1
            else:
                d[l] += 1
        
        for k in ransomNote:
            if k not in d:
                return False
            d[k] -= 1
            if d[k] < 0:
                return False
            
        return True