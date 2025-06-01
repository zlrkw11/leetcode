from typing import List
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        d = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        ans = [""]
        for num in digits:
            s = d[int(num)-2]
            ans = [a+b for a in ans for b in s]
        return ans

# same as:
# for a in ans:
#     for b in s:
#         result.append(a + b)
