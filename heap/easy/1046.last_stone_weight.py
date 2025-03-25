from typing import List
import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        pq = [-stone for stone in stones]
        heapq.heapify(pq)
        while len(pq)>1:

            f = -heapq.heappop(pq)
            s = -heapq.heappop(pq)

            if f != s:
                heapq.heappush(pq,-(f-s))
        return -pq[0] if pq else 0
