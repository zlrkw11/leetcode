class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
       res = nums[0]
       curr_sum = 0
       
       for i in range(len(nums)):
           curr_sum += nums[i]
           res = max(curr_sum, res)
           if curr_sum < 0:
              curr_sum = 0


       return res