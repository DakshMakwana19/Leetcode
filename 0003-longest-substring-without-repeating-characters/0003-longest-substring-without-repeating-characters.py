class Solution(object):
    def lengthOfLongestSubstring(self, s):
        maxi=0
        l=0
        
        last={}
        
        for r in range(len(s)):
            if s[r] in last and last[s[r]] >= l:
                l=last[s[r]]+1
            maxi=max(maxi,r-l+1)
            last[s[r]]=r
        return maxi
       
        