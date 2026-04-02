class Solution:
    def climbStairs(self, n: int) -> int:
        # Base cases for n=1 and n=2
        if n <= 2:
            return n
            
        memo = {1: 1, 2: 2}

        def func(n):
            if n in memo:
                return memo[n]
            else:
                # Recursive step with memoization
                memo[n] = func(n - 2) + func(n - 1)
                return memo[n]

        # This must be aligned with 'memo' and 'def func'
        return func(n)