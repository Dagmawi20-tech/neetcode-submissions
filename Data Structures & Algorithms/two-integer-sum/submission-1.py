class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            n_num = target - nums[i]
            if n_num in seen:
                return [seen[n_num], i]
            seen[nums[i]] = i
                
                
