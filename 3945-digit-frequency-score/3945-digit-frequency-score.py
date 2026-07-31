class Solution(object):
    def digitFrequencyScore(self, n):
        hash={}
        while n:
            digit=n%10
            if digit not in hash:
                hash[digit]=0
            hash[digit]+=1
            n//=10
        score=0
        for digit in hash:
            score+=digit*hash[digit]
        return score
