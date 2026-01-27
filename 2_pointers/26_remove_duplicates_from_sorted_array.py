class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = j = 0
        while j < len(nums):
            if i>0 and nums[j] == nums[i-1]:
                j += 1
            
            else:
                nums[i] = nums[j]
                j+=1
                i+=1

        return i

            