class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice, maxsell = float('inf'), 0

        for price in prices:
            minprice = min(minprice, price)
            maxsell = max(maxsell, price - minprice)

        return maxsell
