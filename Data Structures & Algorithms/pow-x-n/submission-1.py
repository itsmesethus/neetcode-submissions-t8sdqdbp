class Solution:
    def myPow(self, x: float, n: int) -> float:
        # power is zero for any base ==> 1
        if n==0:return 1
        # half calc function
        def half_power(base,exp):
            # if base is 0 ==>0
            if base==0: return 0 
            # if exp is 0 ==>1
            if exp==0: return 1
            # call the function and do the cal for half of its power & multiply it again of half result
            #eg: exp=3 and exp//2 ==>1. so, it will be multiplied twice in next step
            tem=half_power(base,exp//2)
            tem=tem*tem
            # correction part if my n is even everything will be fine.
            # what if n is odd : mulitply the tem with x one more time and give as result
            return tem if exp%2==0 else tem*base
        # right we will handle this n as positive only in the function
        res=half_power(x,abs(n))
        # if n is positive give the result else give it as reciprocal of its.
        # eg: 2^-1 ==> 1/2
        return res if n>0 else 1/res
       