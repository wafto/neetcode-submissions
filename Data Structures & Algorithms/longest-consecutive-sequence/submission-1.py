class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums, longest = set(nums), 0

        for num in nums:
            if num - 1 not in nums:
                tmp, count = num, 0
                
                while tmp in nums:
                    tmp, count = tmp + 1, count + 1
                
                longest = max(longest, count)

        return longest



