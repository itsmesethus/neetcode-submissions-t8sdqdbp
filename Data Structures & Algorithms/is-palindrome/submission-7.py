class Solution:
    def isPalindrome(self, s: str) -> bool:
        # import re
        # s=re.sub(r'[^A-Za-z0-9]','',s).lower()
        # return s==s[::-1]
        d=''.join([x.lower() for x in s if x.isalnum()])
        return d==''.join(reversed(d))
               