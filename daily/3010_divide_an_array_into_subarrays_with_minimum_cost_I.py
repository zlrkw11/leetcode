from typing import List
import heapq
class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0
        
        res = nums[0]
        print(res)
        
        curr = nums[1:]
        heapq.heapify(curr)
        print(curr)
        res += heapq.heappop(curr)
        print(res)
        res += heapq.heappop(curr)
        print(res)
        return res