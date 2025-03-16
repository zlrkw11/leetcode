from typing import List
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        d= {nums[i]:0 for i in range(len(nums))}
    
        for i in range(len(nums)):
            if nums[i] in d:
                d[nums[i]]+=1
        
        for key, value in d.items():
            if value > 1:
                return key
    
solution = Solution()
print(solution.findDuplicate([1,3,4,2,2]))
print(solution.findDuplicate([3,3,3,3,3]))