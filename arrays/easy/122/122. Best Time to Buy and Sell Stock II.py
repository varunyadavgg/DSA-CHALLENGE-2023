class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]
        return profit
    

### OR ###

class Solution(object):
    def maxProfit(self, prices):
        buy = prices[0]
        profit = 0
        
        for currentPrice in prices:
            if currentPrice < buy:
                buy = currentPrice
            else:
                profit += currentPrice - buy
                buy = currentPrice
                
        return profit