class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)

        tmp = 1
        for i in range(len(nums)):
            output[i] *= tmp
            tmp *= nums[i]

        tmp = 1
        for i in range(len(nums) - 1, -1, -1):
            output[i] *= tmp
            tmp *= nums[i]

        return output
        