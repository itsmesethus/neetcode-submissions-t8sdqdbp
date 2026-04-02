class Solution:
    def myPow(self, x: float, n: int) -> float:
        res=1 # res
        # put in for loop for n times and 
        # multiply by base with res
        # if our n is positive return the result else take reciprocal
        for i in range(abs(n)):
            res=res*x
        return res if n>0 else 1/res

        
        