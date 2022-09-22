class Solution:
    def mySqrt(self, x: int) -> int:
        
        
        start = 0
        
        end = x+1
        
        sqrt = 1
        while start < end : 
            
            mid = start+(end-start)//2
            
            sqrt = mid*mid
            
            if sqrt==x:
                return mid
            
            if sqrt > x:
                end = mid
            else:
                start = mid+1
                
        return end-1
                
            
        