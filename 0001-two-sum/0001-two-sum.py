class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        
        dic = {}
        
        for i in range(0,len(nums)):
            p = target - nums[i]
            if p in dic:
                    
                return [dic[p], i]
            else:
                dic[nums[i]] = i
                    