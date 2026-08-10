class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums, longest = set(nums), 0

        for num in nums:
            if num - 1 in nums:
                continue
            curr, length = num, 0
            while curr in nums:
                curr, length = curr + 1, length + 1
            longest = max(longest, length)

        return longest
