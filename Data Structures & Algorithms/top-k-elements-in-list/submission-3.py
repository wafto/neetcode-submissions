class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        bucket = defaultdict(list)
        maxcurr = 0

        for num in nums:
            count[num] += 1
            maxcurr = max(maxcurr, count[num])

        for num, cnt in count.items():
            bucket[cnt].append(num)

        output = []

        while len(output) < k:
            output.extend(bucket[maxcurr])
            maxcurr -= 1

        return output[:k]

        





        
