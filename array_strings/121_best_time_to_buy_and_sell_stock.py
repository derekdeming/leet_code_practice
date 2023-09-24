from typing import List

class Solution: 
    def maxProfit(self, prices: List[int]):
        max_profit = 0
        no_profit = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                max_profit += prices[i] - prices[i-1]

        if max_profit < 0:
            return no_profit
        return max_profit



class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0 
        left = 0 
        right = 1

        while right < len(prices):
            currentProfit = prices[right] - prices[left]
            if prices[left] < prices[right]:
                max_profit = max(currentProfit, max_profit)
            else: 
                left = right 
            right += 1 
        return max_profit 