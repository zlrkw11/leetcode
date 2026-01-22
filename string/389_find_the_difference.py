class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        d1,d2={},{}
        for char in s:
            if char not in d1:
                d1[char] = 1
            elif char in d1:
                d1[char]+=1
        
        for char in t:
            if char not in d1:
                return char
            elif char not in d2:
                d2[char] = 1
            else:
                d2[char]+=1
        
        for key in d2:
            if d1[key] != d2[key]:
                return key
        
     
s = Solution()
s.findTheDifference("abcd", "adbcde")