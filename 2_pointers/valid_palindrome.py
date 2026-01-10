class Solution:
    def isPalindrome(self, s: str) -> bool:
        new = ""
        for c in s:
            if c.isalnum():
                new += c.lower()
        if new == new[::-1]:
            return True
        return False