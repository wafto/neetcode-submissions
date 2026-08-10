class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1

        while left < right:
            addition = numbers[left] + numbers[right]
            
            if addition == target:
                return [left + 1, right + 1]

            if addition < target:
                left += 1
            else:
                right -= 1