class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def getLeft(nums, target):
            l,r = 0, len(nums)-1
            left_idx = -1
            while l <= r:
                mid = l + (r - l) // 2
                if nums[mid] == target:
                    left_idx = mid
                    r = mid - 1  
                elif nums[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
            return left_idx
        def getRight(nums, target):
            l,r = 0, len(nums)-1
            right_idx = -1
            while l <= r:
                mid = l + (r - l) // 2
                if nums[mid] == target:
                    right_idx = mid
                    l = mid + 1 
                elif nums[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
            return right_idx
        res = []
        
        left = getLeft(nums, target)
        right = getRight(nums, target)
        res.append(left)  
        res.append(right)  
        return res