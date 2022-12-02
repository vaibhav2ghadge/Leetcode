import heapq
import sys
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        
        heapq._heapify_max(nums) 
        
        result = None
        k=0
        max_till = -sys.maxsize-1
        while nums:
            p = heapq._heappop_max(nums)
            max_till = max(max_till,p)
            if p!=result:
                k+=1
                result = p
            if k==3:
                return p
        return max_till
                