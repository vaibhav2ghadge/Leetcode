class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        num_element = len(nums)
        
        if num_element==0:
            return -1
        
        start = 0
        
        end = num_element-1
        
        while start <= end:
            
            mid = (start+end)//2
            
            if nums[mid]==target:
                return mid
            
            if nums[mid] <target:
                start = mid+1
            
            else:
                end = mid -1
        return -1
       
                
        
        