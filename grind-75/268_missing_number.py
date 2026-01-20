from typing import List
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        d= set()
        d2 = set()

        for n in range(0, len(nums)+1):
            d.add(n)
        for num in nums:
            d2.add(num)
        res = d.difference(d2)

        if res:
            return res.pop()

        else:
            return 
    
s = Solution()
print(s.missingNumber([0,1]))        