class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        length = len(s)
        for i in range(len(s)):
            for j in range(i, length):
                substring = s[i:j+1]

                if substring == substring[::-1] and len(substring) > len(res):
                    res = substring
        return res 
