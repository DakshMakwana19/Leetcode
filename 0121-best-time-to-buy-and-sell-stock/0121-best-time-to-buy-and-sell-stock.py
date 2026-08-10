class Solution(object):
    def maxProfit(self, prices):
        max=min=prices[0]
        profit=0
        for i in prices:
            if min>i:
                max=min=i
            elif max<i:
                max=i
                tmp=max-min

                if profit<tmp:
                    profit=tmp
        return profit            

        
            

        