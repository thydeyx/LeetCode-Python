class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip()
        if str=="":
            return 0
        else:
            try:
                x=int(str)
                if str[0]=='+' or str[0]=='-':
                    if l>1 and (str[1]>'9' or str[1]<'0'):
                        return 0
                    elif l==1:
                        return 0
            except:
                l=len(str)
                print(str)
                if str[0]>'9' or str[0]<'0' and str[0]!='+' and str[0]!='-':
                    return 0
                if str[0]=='+' or str[0]=='-':
                    if l>1 and (str[1]>'9' or str[1]<'0'):
                        return 0
                    elif l==1:
                        return 0
                if str[0]=='+':
                    pass    
                for i in range(1,l):
                    if str[i]>'9' or str[i]<'0':
                        break;
                if i==(l-1) and '0'<=str[i]<='9':
                    i+=1
                if str[0]=='-':
                    x=int(str[1:i])
                    x=0-x
                elif str[0]=='+':
                    x=int(str[1:i])
                else:
                    x=int(str[0:i])
            if x>2147483647:
                return 2147483647
            elif x<-2147483648:
                return -2147483648
            else:
                return x
