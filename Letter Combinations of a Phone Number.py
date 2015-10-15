d={'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
ans=[]
def dg(digits,k,tmp):
    if k>=len(digits):
        globals()['ans'].append(tmp)
        return
    s=d[digits[k]]
    l=len(s)
    for i in range(l):
        dg(digits,k+1,tmp+s[i])
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits=="":
            return []
        globals()['ans']=[]
        dg(digits,0,"")
        return globals()['ans']
        
