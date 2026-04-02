class Solution:
    def maxProfit(self, prices: List[int]) -> int:
# approach 1:  ( peak and valley) -- greedy approach
        # max_profit=0
        # min_price=float('inf')
        # for price in prices:
        #     if price < min_price:
        #         min_price=min(price,min_price)
        #     profit=price-min_price
        #     if profit > max_profit:
        #          max_profit =max(max_profit,profit)
        # return max_profit
# sliding window:
        max_profit=0
        left,right=0,1
        while right < len(prices):
            if prices[left]<prices[right]:
                profit= prices[right]-prices[left]
                max_profit=max(profit,max_profit)
            else:
                left=right
            right+=1
        return max_profit





           