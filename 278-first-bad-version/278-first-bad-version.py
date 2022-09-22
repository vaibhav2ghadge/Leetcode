# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        
        if n==1:
            return 1
        
        start = 1
        
        end = n
        
        bad_version = -1
        while start <= end:
            
            mid = (start+end)//2
            
            if isBadVersion(mid):
                bad_version = mid
                end = mid-1
            
            else:
                start = mid+1
                
        return bad_version