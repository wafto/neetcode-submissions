class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [0] * (2 * n)

        for i in range(n):
            output[i] = output[i + n] = nums[i]

        return output
        