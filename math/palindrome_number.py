class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        arr = [l for l in x]
        print(arr)
        arr2 = arr[::-1]
        print(arr2)
        if arr == arr2:
            return True
        return False
s = Solution()
print(s.isPalindrome(121))