class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        l=len(s)
        i=0
        ss=[""]*1000
        while i<l:
            j=0
            while j<numRows and i<l:
                ss[j]=ss[j]+s[i]
                j+=1
                i+=1
            j=numRows-2
            while j>0 and i<l:
                ss[j]=ss[j]+s[i]
                j-=1
                i+=1
        ans=""
        for i in range(numRows):
            ans=ans+ss[i]
        return ans

                
            
