"""
Problem: Best Time to Buy and Sell Stock
Link: https://neetcode.io/problems/buy-and-sell-crypto/question

You are given array of stock prices.
Choose best day to buy and sell stock, to maximize profit.
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1: return 0
        start, end, max_profit = 0, 1, 0

        for i, price in enumerate(prices):
            max_profit = max(price - prices[start], max_profit)
            if prices[start] > price:
                start = i
    
        return max_profit
