class Solution(object):
    def largestOddNumber(self, num):
        nums=num[::-1]
        
        for ch in nums:
            if int(ch)%2!=0:
                return num
                break
            num=num[:-1]
        return num
            
            



        