from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r = 0,1
        m = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                p = prices[r] - prices[l]
                m = max(m, p)
            else:
                l=r # new low
            r+=1
        return m
