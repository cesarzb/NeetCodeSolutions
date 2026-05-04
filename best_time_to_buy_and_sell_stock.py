"""
Problem: Best Time to Buy and Sell Stock
Link: https://neetcode.io/problems/buy-and-sell-crypto/question

You are given array of stock prices.
Choose best day to buy and sell stock, to maximize profit.
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest_price, max_profit = prices[0], 0

        for price in prices:
            max_profit = max(max_profit, price - lowest_price)
            lowest_price = min(lowest_price, price)

        return max_profit
