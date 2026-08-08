class Solution(object):
    def minOperations(self, nums, k):
        sum=0
        
        op=0
        for i in range(len(nums)):
            sum+=nums[i]
        while sum%k!=0:
            
            op+=1
            sum-=1
        
        return op




        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        