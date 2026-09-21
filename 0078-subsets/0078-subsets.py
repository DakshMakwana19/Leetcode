class Solution(object):
    def subsets(self, nums):
        result=[[]]
        for i in nums:
            for j in range(len(result)):
                result.append(result[j]+[i])
        return result
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        