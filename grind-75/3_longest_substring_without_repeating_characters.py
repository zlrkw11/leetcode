from typing import Set
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        left = 0
        right = 0
        curr_word = set()
        
        for i in range(right, len(s)):
            
            while s[i] in curr_word:
                curr_word.remove(s[left])
                left+=1

            curr_word.add(s[i])
            res = max(len(curr_word), res)
        return res
       
        
s = Solution()
print(s.lengthOfLongestSubstring("pwwkew"))