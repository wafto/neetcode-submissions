class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = defaultdict(int)
        groups = defaultdict(list)
        output, biggest = [], 0

        for num in nums:
            counter[num] += 1
        
        for num, count in counter.items():
            groups[count].append(num)
            biggest = max(biggest, count)

        while len(output) < k and biggest > 0:
            if biggest in groups:
                output.extend(groups[biggest])
            biggest -= 1

        return output[:k]


