class Solution:
    def sortColors(self, nums: List[int]) -> None:
        i, counts = 0, [0] * 3
        
        for num in nums:
            counts[num] += 1
        
        for color, count in enumerate(counts):
            for _ in range(count):
                nums[i] = color
                i += 1

         
        