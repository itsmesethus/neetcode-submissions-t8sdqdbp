class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # s,t=sorted(s.lower()),sorted(t.lower())
        # if s==t:
        #     return True
        # else: return False
        s,t=list(sorted(s)),list(sorted(t))
        if s==t:
            return True
        else : return False
        
        