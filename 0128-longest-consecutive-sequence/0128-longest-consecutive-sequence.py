class Solution(object):
    def longestConsecutive(self, nums):
        nums.sort()
        maxi=1
        long=1
        if not nums:
            return 0
        for i in range(len(nums)):
            
            if nums[i]==nums[i-1]:
                continue
            if nums[i]==nums[i-1]+1:
                long+=1
            else:
                long=1
            maxi=max(maxi,long)
        return maxi
        """
        :type nums: List[int]
        :rtype: int
        """
        