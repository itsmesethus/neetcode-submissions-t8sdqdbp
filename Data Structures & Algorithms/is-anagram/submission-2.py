class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s=sorted(s.lower())
        t=sorted(t.lower())
        return s==t
        