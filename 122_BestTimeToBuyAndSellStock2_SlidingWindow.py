from typing import List

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy = 0
        sell = 1
        max_p = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                max_p += prices[i] - prices[i-1]
        return max_p


prices = [7,1,5,3,6,4]
Solution().maxProfit(prices)