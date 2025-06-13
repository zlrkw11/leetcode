# solution with hashset
from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        map = set()
        for n in nums:
            if n in map:
                return True
            map.add(n)
        return False

s = Solution()
print(s.containsDuplicate([1,2,3,4,1]))
