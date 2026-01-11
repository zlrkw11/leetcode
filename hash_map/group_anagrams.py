from typing import List 


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for word in strs:
            print("".join(sorted(word)))
            if "".join(sorted(word)) not in d:
                d["".join(sorted(word))] = [word]
            else:
                d["".join(sorted(word))].append(word)
        
        print(d.values())
        return list(d.values())

s = Solution()
print(s.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))