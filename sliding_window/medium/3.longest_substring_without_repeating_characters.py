from collections import Counter
class Solution:
    def lengthOfLongestSubstring(self, s:str)-> int:
        cnt = Counter()
        ans = l = 0
        for r, c in enumerate(s):
            cnt[c] += 1

        return 0

s = Solution()
