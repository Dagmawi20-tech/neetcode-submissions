class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n_nums = sorted(nums)
        count = 1
        best_streak = 1
        if not nums:
                return 0
        for i in range(len(n_nums) - 1):
            if  n_nums[i+1] - n_nums[i] == 1:
                count += 1
            elif n_nums[i+1] - n_nums[i] == 0:
                continue
            else:
                best_streak = max(best_streak, count)
                count = 1
        return max(best_streak, count)