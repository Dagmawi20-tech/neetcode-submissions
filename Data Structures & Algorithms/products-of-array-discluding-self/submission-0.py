class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1] * len(nums)
        right = [1] * len(nums)
        n_list = []
        n = 1
        c = 1
        for i in range(len(nums)):
            left[i] = n
            n *= nums[i]
        for i in range(len(nums) -1, -1, -1):
            right[i] = c
            c *= nums[i]
        for d in range(len(left)):
            n_list.append(left[d] * right[d])
        return n_list

