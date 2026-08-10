class Solution(object):
    def maxProfit(self, prices):
        maxprofit=0
        l=0
        
        for i in range(len(prices)):
            if prices[l]>prices[i]:
                l=i
            else:
                profit=prices[i]-prices[l]
                maxprofit=max(maxprofit,profit)
        return maxprofit
                
            

        
            

        