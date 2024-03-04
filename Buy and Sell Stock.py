class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p=0
        i=0
        j=1
        while j<len(prices):
            cp=prices[j]-prices[i]
            #if prices[i]>prices[j]:
            #    break
            if prices[i]<prices[j]:
                p=max(cp,p)
            else:
                i=j
            j+=1
        return p
