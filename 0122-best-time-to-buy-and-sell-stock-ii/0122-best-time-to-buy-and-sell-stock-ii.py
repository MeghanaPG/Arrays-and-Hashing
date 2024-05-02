class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Time complexity: O(n)
        max_profit = 0
        
        for i in range(1, len(prices)):
            # If there's a potential profit opportunity
            if prices[i] > prices[i - 1]:
                max_profit += prices[i] - prices[i - 1]
                
        return max_profit

        