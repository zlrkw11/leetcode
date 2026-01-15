# 描述： 给定一个整数数组 nums（代表每天的交易金额）和一个整数 k。 
# 你需要找出长度为 k 的连续子数组，使得该子数组的平均金额最大，并返回该最大平均值。
class Solution:
    def maxAverageSlice(self, nums:int, k:int) -> int:
        res = -float('inf')
        
        i = 0
        j = k+1

        while j < len(nums):
            curr_sum = sum(nums[i:j])
            j += 1
            i += 1
            res = max(res, curr_sum)

        return res/k