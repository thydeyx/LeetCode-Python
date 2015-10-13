class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        s=str(x)
        l=list(s)
        l.reverse()
        sq=''
        s1=sq.join(l)
        if s==s1:
            return True
        else:
            return False
        
