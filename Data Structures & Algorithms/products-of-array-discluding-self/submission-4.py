class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = [] 
        r = [1] * len(nums)
        p_r = 1
        p_l = 1
        t = []
        for i in range(len(nums)):
            l.append(p_l)
            p_l *= nums[i]
        for i in range(len(nums)-1, -1, -1):
            r[i] = p_r
            p_r*=nums[i]
        for i in range(len(nums)):
            t.append(l[i] * r[i])
        return t


