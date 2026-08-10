# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        self.quickSortHelper(pairs, 0, len(pairs) - 1)
        return pairs

    def quickSortHelper(self, data: List[Pair], start: int, end: int) -> None:
        if end - start + 1 <= 1:
            return

        pivot = data[end]
        left = start

        for i in range(start, end):
            if data[i].key < pivot.key:
                data[i], data[left] = data[left], data[i]
                left += 1

        data[end] = data[left]
        data[left] = pivot
            
        self.quickSortHelper(data, start, left - 1)
        self.quickSortHelper(data, left + 1, end)