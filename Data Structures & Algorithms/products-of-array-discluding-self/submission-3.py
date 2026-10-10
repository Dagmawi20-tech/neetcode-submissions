class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_total = []
        right_total = [1] * len(nums)
        pr_l = 1
        pr_r = 1
        t = []
        for i in range(len(nums)):
            left_total.append(pr_l)
            pr_l *= nums[i]

        for i in range(len(nums)-1,-1,-1):
            right_total[i] = pr_r
            pr_r *= nums[i]

        for i in range(len(nums)):
            t.append(left_total[i] *  right_total[i])
        return t



