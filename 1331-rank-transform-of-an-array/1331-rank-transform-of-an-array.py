class Solution(object):
    def arrayRankTransform(self, arr):
        temp=sorted(set(arr))
        rank={}
        for i in range(len(temp)):
            rank[temp[i]]=i+1
        for i in range(len(arr)):
            arr[i]=rank[arr[i]]
        return arr
        
        
        