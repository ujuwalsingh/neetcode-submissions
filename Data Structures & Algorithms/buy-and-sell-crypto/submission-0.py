class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cost = 0
        for i in range (len(prices)):
            for j in range (i+1, len(prices)):
                cost = max(cost, prices[j] - prices[i])
        return cost