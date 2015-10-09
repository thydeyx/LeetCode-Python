class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n=len(s)
        #if n==0 return ''
        longest = s[0:1]
        for i in range(n-1):
            l=i
            r=i
            while l>=0 and r<=n-1 and s[l]==s[r]:
                l-=1
                r+=1
            if len(s[l+1:r])>len(longest):
                longest=s[l+1:r]
            l=i
            r=i+1
            while l>=0 and r<=n-1 and s[l]==s[r]:
                l-=1
                r+=1
            if len(s[l+1:r])>len(longest):
                longest=s[l+1:r]
        return longest
