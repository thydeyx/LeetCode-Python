from collections import deque
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l=len(s)
        q=deque()
        for i in range(l):
            f=True
            if s[i]=='[' or s[i]=='{' or s[i]=='(':
                q.append(s[i])
            else:
                try:
                    ch=q.pop()
                except:
                    return False
                if s[i]==']' and ch!='[':
                    f=False
                elif s[i]=='}' and ch!='{':
                    f=False
                elif s[i]==')' and ch!='(':
                    f=False
            if f==False:
                break
        if f==False:
            return f
        else:
            try:
                q.pop()
                return False
            except:
                pass
        return True
        
        
