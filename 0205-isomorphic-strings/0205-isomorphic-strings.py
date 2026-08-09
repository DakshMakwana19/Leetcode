class Solution(object):
    def isIsomorphic(self, s, t):
        hash={}
        for i in range(len(s)):
            if s[i] in hash:
                if hash[s[i]]!=t[i]:
                    return False
            else:
                if t[i] in hash.values():
                    return False
                hash[s[i]]=t[i]
        return True
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        