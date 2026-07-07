class Solution(object):
    def sumAndMultiply(self, n):
        n=str(n)
        sumu=0
        k=""
        for ch in n:
            if ch=="0":
                continue
            k+=ch   
            sumu+=int(ch)
        if k=="":
            return 0
        return int(k)*sumu
            


        """
        :type n: int
        :rtype: int
        """
        