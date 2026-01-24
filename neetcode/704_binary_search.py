from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1

        #continue going until 0 possibilities left
        while l <= r:
            m=(l+r)//2
            if nums[m] > target:
                r = m-1
            elif nums[m] > target:
                l = m+1
            else:
                return m
            
        return -1

    
s=Solution()
s.search([8,3,4,1], 4)