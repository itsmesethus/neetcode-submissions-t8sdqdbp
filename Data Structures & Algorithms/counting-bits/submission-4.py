class Solution:
    def countBits(self, n: int) -> List[int]:
        res=[]
        for i in range(n+1):
            b=i.bit_count()
            res.append(b)
        return res
        