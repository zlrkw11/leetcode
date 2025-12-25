from typing import List

class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        total_sum = 0

        for i in range(k):
            curr = happiness[i] - i # minus 1 every round until K

            if curr > 0:
                total_sum += curr

            else:
                break
                    
        return total_sum