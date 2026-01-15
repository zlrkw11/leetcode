from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}

        for i in range(len(nums)):
            num = nums[i]
            comp = target - num
            if comp in d:
                return [i, d[comp]]
            else:
                d[num] = i
            
s = Solution()

print(s.twoSum([2,7,11,15], 9))