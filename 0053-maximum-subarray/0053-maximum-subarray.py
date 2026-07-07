class Solution(object):
    def maxSubArray(self, nums):
        current=0
        maximum=nums[0]
        for num in nums:
            current+=num
            if current>maximum:
                maximum=current
            if current<0:
                current=0
        return maximum

                    
        
        