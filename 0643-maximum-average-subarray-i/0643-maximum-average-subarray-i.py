class Solution(object):
    def findMaxAverage(self, nums, k):
        sumu=0
        for i in range(k):
            sumu+=nums[i]
        maxi=sumu
        for i in range(k,len(nums)):
            sumu+=nums[i]-nums[i-k]
            maxi=max(maxi,sumu)
        return maxi/float(k)