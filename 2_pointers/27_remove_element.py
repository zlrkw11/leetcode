class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        i = j = 0
        while j < len(nums):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
            j += 1
        return i
    
s = Solution()
print(s.removeElement([3,2,2,3]))