class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [[1000 - n, n] for n in nums]
        heapq.heapify(nums)
        i = 1
        while i <= k:
            _, n = heapq.heappop(nums)
            if i == k:
                return n
            i += 1 
