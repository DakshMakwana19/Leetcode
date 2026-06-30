class Solution(object):
    def reverse(self, x):
        sign=1
        if x<0:
            sign=-1
        x=abs(x)
        x=str(x)
        x=x[::-1]
        x=int(x)
        x*=sign
        if x<-2**31 or x>2**31-1:
            return 0

        return x        