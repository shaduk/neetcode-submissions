class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minSofar = 1000
        maxProfit = 0
        for price in prices:
            minSofar = min(price, minSofar)
            maxProfit = max(price-minSofar, maxProfit)
        return maxProfit