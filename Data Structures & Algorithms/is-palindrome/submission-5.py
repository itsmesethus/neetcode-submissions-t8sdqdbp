class Solution:
    def isPalindrome(self, s: str) -> bool:
        import re
        s=s.lower()
        s=re.sub(r'[^A-Za-z0-9]','',s)
        return s==s[::-1]