class Solution:
    def hammingWeight(self, n: int) -> int:
        c=0
        bins_n=bin(n)
        for i in range(len(bins_n)):
            if bins_n[i]=='1':
                c+=1
        return c
        