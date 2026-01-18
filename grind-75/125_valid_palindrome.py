class Solution:
    def isPalindrome(self, s: str) -> bool:
        st = "" 
        for char in s:
            if char.isalnum():
                st+=char.lower()
        i = 0
        j = len(st)-1

        while i < j:
            if st[i] != st[j]:
                return False
            else:
                i += 1
                j -= 1
        return True