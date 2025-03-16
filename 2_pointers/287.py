from typing import List
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1
        while left < len(nums) and right > -1:
            if nums[left] == nums[right]:
                return nums[left]
            left += 1
            right -= 1

        return 
    
solution = Solution()
print(solution.findDuplicate([1,3,4,2,2]))