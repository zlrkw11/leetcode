class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
       left = res = 0
       curr_word = set()
       for right in range(len(s)):
            
            while s[right] in curr_word:
                curr_word.remove(s[left])
                left += 1

            curr_word.add(s[right])

            res = max(res, len(curr_word))
           
       return res 