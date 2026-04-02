class Solution:
    def countBits(self, n: int) -> List[int]:
        res=[]
        for  i in range(n+1):
            temp_i=i
            temp_count_i=0
            while temp_i!=0:
                temp_count_i+=(temp_i%2)
                temp_i=temp_i//2
            res.append(temp_count_i)
            temp_count_i=0
        return res
        