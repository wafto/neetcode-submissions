class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans, curr = 0, 0
        prefix = {0: 1}

        for num in nums:
            curr += num
            diff = curr - k
            ans += prefix.get(diff, 0)
            prefix[curr] = prefix.get(curr, 0) + 1

        return ans