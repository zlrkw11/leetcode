class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums:
            return False
         
        def jump(i):
            if nums[i] == 0 and i != len(nums)-1:
                return False 
            else: 
                i = i + nums[i]
        i = 0
        while i < len(nums)-1:
            jump(i)                
        
        return True