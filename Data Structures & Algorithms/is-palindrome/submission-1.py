class Solution:
    def isPalindrome(self, s: str) -> bool:
        import re
        fil= re.sub(r'[^A-Za-z0-9]', "",s).lower()
        return fil==fil[::-1]