class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = defaultdict(int)
        bucket = defaultdict(list)
        largest, output = 0, []

        for num in nums:
            counter[num] += 1

        for num, count in counter.items():
            bucket[count].append(num)
            largest = max(largest, count)
        
        while len(output) < k and largest > 0:
            if largest in bucket:
                output.extend(bucket[largest])
            largest -= 1

        return output[:k]
        
