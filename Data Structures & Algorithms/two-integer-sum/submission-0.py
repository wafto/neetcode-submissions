class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary = {}

        for i, num in enumerate(nums):
            search = target - num
            if search in dictionary:
                return [dictionary[search], i]
            dictionary[num] = i

        return []