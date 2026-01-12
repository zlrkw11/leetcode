class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        j = 0
        res = 0
    
        while j < len(s):
            curr = s[i:j]
            if s[j] not in curr:
                j += 1
                res = max(res, j-i)
            else:
                i += 1
            
        return res
    
s = Solution()
print(s.lengthOfLongestSubstring("abcabcbb"))

# a b c