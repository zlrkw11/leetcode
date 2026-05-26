class Solution(object):
    def twoSum(self, nums, target):
     
        d = {}

        for i,n in enumerate(nums):
            dif = target - n
            # if dif is a key 
            if dif in d:
                return [d[dif], i]
            
            d[n] = i 
        
        return []