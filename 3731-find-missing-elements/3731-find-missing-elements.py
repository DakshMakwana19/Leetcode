class Solution(object):
    def findMissingElements(self, nums):
        
        sety=set(nums)
        
        minu=min(nums)
        maxu=max(nums)
        ans=[]
        for i in range(minu,maxu+1):
            if i not in sety:
                ans.append(i)
        return ans

           

        
   
        