class Solution(object):
    def maxProduct(self, n):
        n=str(n)
        x=''.join(sorted(n, reverse=True))
        a=int(x[0:1])
        b=int(x[1:2])
        return a*b


        
        

       
        