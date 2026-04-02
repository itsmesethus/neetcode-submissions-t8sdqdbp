class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        m=set()
        lf=0
        res=0
        for rf in range(len(s)):
            while s[rf] in m:
                m.remove(s[lf])
                lf+=1
            m.add(s[rf])
            res=max(res,rf-lf+1)
        return res

                
          

        