class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        if k > len(nums):
            return 0 
        i = 0
        j = k
        
        curr_sum = sum(nums[:k])
        max_sum = curr_sum
        while j < len(nums):
            curr_sum += nums[j]
            curr_sum -= nums[i]
            print(curr_sum)
            max_sum = max(curr_sum, max_sum)
            j+=1
            i+=1 
                   
        return max_sum/k
    
s = Solution()
print(s.findMaxAverage([1,2,3,4,5], 2))