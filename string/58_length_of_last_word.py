class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        word_arr = s.lower().split()
        print(word_arr)
        return len(word_arr[-1])
    
s=Solution()
s.lengthOfLastWord("Hello World")