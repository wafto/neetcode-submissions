class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0

        maxsum = nums[0]
        curr = 0

        for n in nums:
            curr = n + max(0, curr)
            maxsum = max(maxsum, curr)
        
        return maxsum