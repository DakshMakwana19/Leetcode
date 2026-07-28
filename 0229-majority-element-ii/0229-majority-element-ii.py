class Solution(object):
    def majorityElement(self, nums):
        hash={}
        n=len(nums)
        k=n//3
        result=set()
        for num in nums:
            if num not in hash:
                hash[num]=0
            hash[num]+=1
            if hash[num]>k:
                result.add(num)
        return list(result)
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        