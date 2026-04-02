class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left=0
        max_profit=0
        right=1
        while right < len(prices):
            if prices[right]>prices[left]:
                profit=prices[right]-prices[left]
                max_profit=max(max_profit,profit)
            elif prices[left]>prices[right]:
                left=right
            right+=1
        return max_profit


        