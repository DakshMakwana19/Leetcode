class Solution(object):
    def totalFruit(self, fruits):
        l=0
        r=0
        
        maxlen=0
        num={}
        while r<len(fruits):

            if fruits[r] not in num:
                num[fruits[r]]=0
            num[fruits[r]]+=1
            
            while(len(num)>2):
                num[fruits[l]]-=1
                    
                if num[fruits[l]]==0:
                    del num[fruits[l]]
                l+=1
            
            maxlen=max(maxlen,r-l+1)
            r+=1
        return maxlen


            
          
        
        
        