class Solution:
    def longestPalindrome(self, s: str) -> int:
        if not s:
            return 0
        d = {}
        count= 0
        odd = False
        for letter in s.lower():
            if letter not in d:
                d[letter] = 1
            else:
                d[letter] += 1
        print(d)
        
        for item in d.values():
            if item % 2==0:
                count += item
            else:
                count += item-1
        return count + 1 if odd else count


s = Solution()
print(s.longestPalindrome("abcabccc"))