class Solution(object):
    def isIsomorphic(self, s, t):
        forward={}
        reverse={}
        for i in range(len(s)):
            a=s[i]
            b=t[i]
            if a in forward and forward[a]!=b:
                return False
            else:
                forward[a]=b
                    
            if b in reverse and reverse[b]!=a:
                return False
            else:
                reverse[b]=a
        return True
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        