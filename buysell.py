class Solution:
    def maxProfit(self, prices: list[int], fee: int) -> int:
        hold, cash = -prices[0], 0
        for price in prices[1:]:
            cash = max(cash, hold + price - fee)
            hold = max(hold, cash - price)
        return cash
