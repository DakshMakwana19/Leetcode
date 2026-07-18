class Solution(object):
    def leftRightDifference(self, nums):
        n=len(nums)
        rsum=sum(nums)
        lsum=0
        arr=[0]*n
        for i in range(n):
            rsum-=nums[i]
            arr[i]=abs(lsum-rsum)
            
            lsum+=nums[i]
            
        return arr

        """
        :type nums: List[int]
        :rtype: List[int]
        """
        