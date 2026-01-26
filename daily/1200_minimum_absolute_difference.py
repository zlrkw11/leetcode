from typing import List
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        sorted_arr = sorted(arr)
        min_dif = 10000
        res = []
        for i in range(0, len(sorted_arr)-1):
            min_dif = min(min_dif, sorted_arr[i+1] - sorted_arr[i])

        for i in range(0, len(sorted_arr)-1):
            if sorted_arr[i+1] - sorted_arr[i] == min_dif:
                res.append([sorted_arr[i], sorted_arr[i+1]])
        return res