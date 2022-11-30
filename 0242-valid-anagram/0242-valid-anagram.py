class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        dic = {}
        
        for sp in s:
            
            if sp not in dic:
                dic[sp] = 1
            else:
                
                dic[sp] +=1
        for sp in t:
            
            if sp not in dic or dic[sp]==0:
                return False
            else:
                dic[sp] -=1
        return True
        