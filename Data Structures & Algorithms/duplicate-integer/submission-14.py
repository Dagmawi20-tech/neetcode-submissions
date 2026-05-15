class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))

solution = Solution()
nums = [1, 2, 3, 4, 5]
print(solution.hasDuplicate(nums))  # False

nums = [1, 2, 3, 1]
print(solution.hasDuplicate(nums))  # True

