class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxStore, currStore = 0, 0
        left, right = 0, len(heights) - 1

        while left < right:
            currStore = min(heights[left], heights[right]) * (right - left)
            maxStore = max(maxStore, currStore)

            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1

        return maxStore