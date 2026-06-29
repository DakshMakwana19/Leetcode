class Solution(object):
    def isPerfectSquare(self, num):
        import math
        n=math.sqrt(num)
        if int(n)==n:
            return True
        return False
        