class Solution:
    def climbStairs(self, n: int) -> int:
        if n <=2:
            return n

        dp=[0]*n
        dp[0]=1
        dp[1]=2
        for vals in range(2,n):
            dp[vals]=dp[vals-2]+dp[vals-1]
        return dp[n-1]
        