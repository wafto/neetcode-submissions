class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        major, count = nums[0], 0

        for num in nums:
            if num == major:
                count += 1
            else:
                count -= 1

            if count <= 0:
                major = num

        return major
            