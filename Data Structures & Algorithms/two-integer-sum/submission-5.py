class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} # val : index 
        for value, index in enumerate(nums):
            diff = target - index
            if diff in seen:
                return [seen[diff], value]
            else:
                seen[index] = value
               