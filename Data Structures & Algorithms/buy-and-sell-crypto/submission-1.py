class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        l = 0
        r = 0
        while r < len(prices):
            if prices[l] > prices[r]:
                print(prices[l], prices[r], 0)
                l += 1
                continue
            profit = prices[r] - prices[l]
            print(prices[l], prices[r], profit)
            maxProfit = max(maxProfit, profit)
            r += 1
            
        return maxProfit


# 10, 1, 5, 6, 7, 1
#     l
#                   r