class Solution:
    def myPow(self, x: float, n: int) -> float:
        # 
        if n==0:return 1

        def half_power(base,exp):
            if base==0: return 0
            if exp==0: return 1

            tem=half_power(base,exp//2)
            tem=tem*tem
              
            return tem if exp%2==0 else tem*base

        res=half_power(x,abs(n))

        return res if n>0 else 1/res
       