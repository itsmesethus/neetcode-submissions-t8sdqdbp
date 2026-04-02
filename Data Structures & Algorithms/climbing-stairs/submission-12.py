class Solution:
    #Bottom-Up Dynamic Programming logic that interviewers love to see.
    def climbStairs(self, n: int) -> int:
        if n <=2:
            return n

        dp=[None]*n
        dp[0]=1
        dp[1]=2

        for vals in range(2,n):
            dp[vals]=dp[vals-2]+dp[vals-1]
        return dp[-1]
        