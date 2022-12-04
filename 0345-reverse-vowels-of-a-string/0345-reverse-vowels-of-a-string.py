class Solution:
    def reverseVowels(self, s: str) -> str:
        
        s = list(s)
        start =0
        end =len(s)-1
        
        l = len(s)
        while start < end:
            
            while start<end:
                
                c = s[start].lower()
                if c=='a' or c=='e' or c=='i' or c=='o' or c=='u':
                    break
                start+=1
            
        
            while end >start:
                c = s[end].lower()
                if c=='a' or c=='e' or c=='i' or c=='o' or c=='u':
                    break
                end-=1
            
            if start==end:
                break
            if start!=end:
                t = s[start]
                s[start] = s[end]
                s[end]=t
                start +=1
                end-=1
            
        return ''.join(s)
                
                
        