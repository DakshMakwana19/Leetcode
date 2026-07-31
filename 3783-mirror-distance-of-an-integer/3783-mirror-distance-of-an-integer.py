class Solution(object):
    def mirrorDistance(self, n):
        r=int(str(n)[::-1])
        return abs(n-r)
        
        