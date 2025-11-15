
from typing import List

# [1,0,2] [1,0,2,4,2]
class Solution:
    def candy(self, ratings: List[int]) -> int:
        arr = [1 for i in range(len(ratings))]
        if len(arr)<2:
            return 1
        if len(arr) == 0:
            return 0
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                arr[i] = arr[i-1] + 1
        
        for i in range(len(ratings)-2,-1, -1):
            if ratings[i] > ratings[i+1]:
                arr[i] = max(arr[i], arr[i+1]+1)
                
        return sum(arr)
s = Solution()
print(s.candy([29,51,87,87,72,12]))

# 1 2 3 3 2 1