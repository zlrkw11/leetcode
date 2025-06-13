# mod by 2
# shift every bit to right by 1
class Solution:
    def hammingWeight(self, n:int)->int:
        res = 0
        while n:
            res += n % 2
            n = n >> 1
        return res
