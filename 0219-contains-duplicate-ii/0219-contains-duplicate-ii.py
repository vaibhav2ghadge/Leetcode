class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        dic = {}
        for i in range(0,len(nums)):
            
            if nums[i] in dic:
                if (abs(dic[nums[i]] - i)<=k):
                    return True
                else:
                    dic[nums[i]] = i
            else:
                dic[nums[i]] = i
        return False
        