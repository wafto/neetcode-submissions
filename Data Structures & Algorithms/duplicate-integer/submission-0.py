class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        encounters = set()
        for num in nums:
            if num in encounters:
                return True
            encounters.add(num)
        return False