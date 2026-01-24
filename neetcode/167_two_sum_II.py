class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        d = {}
        for i,n in enumerate(numbers):
            if n not in d:
                d[n] = i
                
            if target-n in d and d[target-n] != i:
                return [d[target-n]+1, i+1]
        return []