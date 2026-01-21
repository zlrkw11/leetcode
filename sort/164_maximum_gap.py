from typing import List
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums)<2:
            return 0
        max_value = 0
        i = 0
        sorted_nums = sorted(nums)
        while i < len(sorted_nums) -1:
            max_value = max(sorted_nums[i+1]-sorted_nums[i], max_value)
            i+=1
        
        return max_value
    

s = Solution()
print(s.maximumGap([3,6,9,1]))