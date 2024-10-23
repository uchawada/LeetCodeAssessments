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

        while sell < len(prices):
            if prices[buy] < prices[sell]:
                p = prices[sell] - prices[buy]
                max_p = max(p, max_p)
            else:
                buy += 1
            sell += 1
        return max_p


prices = [7,1,5,3,6,4]
Solution().maxProfit(prices)