from typing import List 


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for word in strs:
            print("".join(sorted(word)))
            t = "".join(sorted(word))
            if t not in d:
                d[t] = [word]
            else:
                d[t].append(word)
        
        print(d.values())
        return list(d.values())

s = Solution()
print(s.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))