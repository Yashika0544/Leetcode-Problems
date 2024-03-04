class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p=[]
        for i in range(len(prices)-1):
            if prices[i]<prices[i+1]:
                p.append(prices[i+1]-prices[i])
        return sum(p)
