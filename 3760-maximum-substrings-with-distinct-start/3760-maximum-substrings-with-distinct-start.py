class Solution(object):
    def maxDistinct(self, s):
        hash={}
        for ch in s:
            if s not in hash:
                hash[ch]=0
            hash[ch]+=1
        return len(hash)
        