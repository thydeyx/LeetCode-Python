import sys
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        l=len(strs)
        if l==0:
            return ""
        if l==1:
            return strs[0]
        m=sys.maxsize
        ans=0
        for i in range(l):
            if len(strs[i])<m:
                m=len(strs[i])
        #print(m)
        for i in range(m):
            ch=strs[0][i]
            f=True
            for j in range(1,l):
               if ch!=strs[j][i]:
                   f=False
                   break
            if f==False:
                break
        ans=i
        if ans==(m-1): ans+=1
        return strs[0][0:ans]
        
