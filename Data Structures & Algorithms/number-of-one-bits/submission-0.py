class Solution:
    def hammingWeight(self, n: int) -> int:
        res=0
        while n:
            res+=n%2
            n=n>>1   # we're shifting the '1' to the right side one by one 
        return res