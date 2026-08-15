class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counter = defaultdict(int)
        threshold = len(nums) // 3 + 1

        for num in nums:
            counter[num] += 1
        
        return [num for num, count in counter.items() if count >= threshold]


        

        