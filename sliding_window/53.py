from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
       maxSub = nums[0]
       curr = 0
       for n in nums:
           if curr < 0:
               curr = 0
           curr += n
           maxSub = max(maxSub, curr)
       return maxSub

solution = Solution()
print(solution.maxSubArray([1,2,3,4,5,-1]))