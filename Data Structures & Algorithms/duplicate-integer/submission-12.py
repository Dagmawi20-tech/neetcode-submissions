class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        new_list= set()
        for i in nums:
            if i in new_list:
                return True
            else:
                new_list.add(i)
        return False

solution = Solution()
nums = [1, 2, 3, 4, 5]
print(solution.hasDuplicate(nums))  # False

nums = [1, 2, 3, 1]
print(solution.hasDuplicate(nums))  # True

