class Solution(object):
    def concatWithReverse(self, nums):
        n=len(nums)
        nums1=nums[::-1]
        return nums+nums1
        