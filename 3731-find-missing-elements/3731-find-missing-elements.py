class Solution(object):
    def findMissingElements(self, nums):
        
        nums.sort()
        
        minu=min(nums)
        maxu=max(nums)
        ans=[]
        for num in range(minu,maxu+1):
            if num not in nums:
                ans.append(num)
        return ans

           

        
   
        