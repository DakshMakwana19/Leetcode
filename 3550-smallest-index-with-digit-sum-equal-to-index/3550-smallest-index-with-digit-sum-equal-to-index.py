class Solution(object):
    def smallestIndex(self, nums):
        index=0
        
        for i in nums:
            sum=0
            
            while i>0:
                sum+=i%10
                i//=10
            
            if sum==index:
                return sum
            index+=1
        return -1

        
        """
        :type nums: List[int]
        :rtype: int
        """
        