class Solution(object):
    def maxVowels(self, s, k):
        vowel="aeiou"
        maxi=0
        for i in range(k):
            if s[i] in vowel:
                maxi+=1
        sumu=maxi
        for i in range(k,len(s)):
            if s[i-k] in vowel:
               maxi-=1
            if s[i] in vowel:
                maxi+=1
            sumu=max(sumu,maxi)
        return sumu

        """
        :type s: str
        :type k: int
        :rtype: int
        """
        