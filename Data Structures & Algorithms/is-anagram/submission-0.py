class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s,t=sorted(s.lower()),sorted(t.lower())
        if s==t:
            return True
        else: return False
        