# contains duplicate
from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d = {}
        for i,n in enumerate(nums):
            if n not in d:
                d[n] = 1
            else:
                return True
        return False

s = Solution()
print(s.containsDuplicate([1,2,3,4,1]))
