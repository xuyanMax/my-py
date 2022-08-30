# You may complete as many transactions as you like,
# but you need to pay the transaction fee for each transaction.
# You may not buy more than 1 share of a stock at a time (ie. you must sell the stock share before you buy again.)
#
# Return the maximum profit you can make.
#
# Example 1:
# Input: prices = [1, 3, 2, 8, 4, 9], fee = 2
# Output: 8
# Explanation: The maximum profit can be achieved by:
# Buying at prices[0] = 1
# Selling at prices[3] = 8
# Buying at prices[4] = 4
# Selling at prices[5] = 9
# The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.


class BestTimeBuySellStockWithTransactionFee(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        tik0, tik1=0, -prices[0]
        for i in range(1, len(prices)):
            tmp = tik0
            tik0 = max(tik0, tik1 + prices[i] - fee)
            tik1 = max(tik1, tmp - prices[i])
        return tik0
