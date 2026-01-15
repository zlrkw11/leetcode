class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        j = 0
        res = 0
        while j < len(s):
            curr_word = s[i:j]
            print(curr_word)
            if s[j] not in curr_word:
                j += 1
            else: 
                i += 1
            res = max(len(curr_word), res)
        return res
    

s = Solution()
print(s.lengthOfLongestSubstring("zxyzyx"))