class Solution:
    def countBits(self, n: int) -> List[int]:
        res=[]
        for i in range(n+1):
            bit_s=i.bit_count()
            res.append(bit_s)
        return res

        