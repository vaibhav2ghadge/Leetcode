class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        
        if (len(s)>len(t)):
            return False
        
        if(len(s)==0):
            return True
        
        p = len(s)-1
        for i in range(len(t)-1,-1,-1):
            
            if s[p] == t[i]:
                p-=1
                if p==-1:
                    return True
        return False
        