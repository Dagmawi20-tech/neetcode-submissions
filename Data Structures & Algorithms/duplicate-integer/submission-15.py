class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        count = 0
        for i in range(len(nums)):
            if nums[i] in seen:
                count +=1
            else:
                seen.add(nums[i])
        return count != 0