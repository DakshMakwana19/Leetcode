class Solution(object):
    def minSubArrayLen(self, target, nums):
        l=0
        r=0
        sum=0
        minlen=len(nums)+1
        for r in range(len(nums)):
            sum+=nums[r]
            while target<=sum:
                
                minlen=min(minlen,r-l+1)
                sum-=nums[l]
                l+=1
        if minlen==len(nums)+1:
            return 0
        return minlen
        