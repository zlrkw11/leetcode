import heapq
from typing import List
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        d = set()
        for num in nums: 
            if num not in d:
                d.add(num)
        print(d)
        min_heap = []
        if len(d) < 3:
            print(list(d)[-1])
            return max(d)
        for num in d:
            print(min_heap)
            heapq.heappush(min_heap, num)
            if len(min_heap) > 3:
                heapq.heappop(min_heap)
            
        return min_heap[0]

s = Solution()
print(s.thirdMax([3,2,1]))