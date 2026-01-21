class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        d = {}

        for num in nums:
            if num not in d:
                d[num] = 1
            else:
                d[num]+=1

        for key in d.keys():
            if d[key] == 1:
                return key
