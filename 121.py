# TIME LIMIT EXCEEDED
class Solution(object):
    def maxProfit(self, prices):
        res = 0
        for i in range(len(prices)):
            if prices[i+1:]:
              res = max(res, max(prices[i+1:]) - prices[i])
        return res
