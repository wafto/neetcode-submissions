class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums or target < nums[0] or target > nums[len(nums) - 1]:
            return -1

        left = 0
        right = len(nums) - 1

        while left <= right:
            middle = left + (right - left) // 2

            if nums[middle] == target:
                return middle
            
            if target < nums[middle]:
                right = middle - 1
            else:
                left = middle + 1
        
        return -1
            