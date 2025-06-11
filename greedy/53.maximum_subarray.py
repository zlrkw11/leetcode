from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        i = 0
        mx = 0
        for item in nums:
            if mx > nums[i]+mx:
                i+=1
            else:
                mx = nums[i]+mx
        return mx

s = Solution()
print(s.maxSubArray([5,4,-1,7,8]))
