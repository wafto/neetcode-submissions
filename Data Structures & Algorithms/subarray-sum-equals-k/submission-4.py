class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ps, ans, curr = defaultdict(int), 0, 0
        ps[0] = 1

        for num in nums:
            curr += num
            diff = curr - k
            ans += ps[diff]
            ps[curr] += 1

        return ans