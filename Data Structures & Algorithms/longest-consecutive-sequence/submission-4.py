class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n_nums = set(nums)
        best_streak = 0
        for i in n_nums:
            if i - 1 not in n_nums:
                current = i
                count = 1
                while current + 1 in n_nums:
                    current += 1
                    count += 1
                best_streak = max(best_streak, count)
        return best_streak
