class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # min_price=float('inf')
        # max_profit=0

        # for price in prices:
        #     if price < min_price:
        #         min_price=price
        #     profit = price- min_price

        #     if profit > max_profit:
        #         max_profit = profit
        # return max_profit

        max_profit=0
        min_price=float('inf')
        for price in prices:
            if price < min_price:
                min_price=min(price,min_price)
            profit=price-min_price
            if profit > max_profit:
                 max_profit =max(max_profit,profit)
        return max_profit


           