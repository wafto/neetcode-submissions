class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [0] * n

        prev = 1
        for i in range(n):
            output[i] = prev
            prev *= nums[i]
        
        prev = 1
        for i in range(n - 1, -1, -1):
            output[i] *= prev
            prev *= nums[i]

        return output
