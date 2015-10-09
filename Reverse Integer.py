import sys
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        mid=list(str(x))
        if len(mid)==1:
            return x
        if mid[0]>'9' or mid[0]<'0':
            temp=mid[1:len(mid)]
            temp.reverse()
            temp.insert(0,mid[0])
        else:
            mid.reverse()
            temp=mid
        mid=temp
        sq=''
        x=int(sq.join(mid))
        if x>2147483646 or x<-2147483647:
            return 0
        else:
            return x
