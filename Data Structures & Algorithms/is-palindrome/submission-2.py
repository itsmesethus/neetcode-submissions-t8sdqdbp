class Solution:
    def isPalindrome(self, s: str) -> bool:
        import re
        s=re.sub(r'[^A-Za-z0-9]','',s)
        s=s.lower()
    
        return s==s[::-1]
        