class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s = s.lower()
        t = t.lower()
        
        d1, d2 = {}, {}
        
        for l in s:
            if l in d1:
                d1[l] += 1
            else:
                d1[l] = 1

        for l in t:
            if l in d2:
                d2[l] += 1
            else:
                d2[l] = 1
        
        return d1 == d2

      
            

    


    

