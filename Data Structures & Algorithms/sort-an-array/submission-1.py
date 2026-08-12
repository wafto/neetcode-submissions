class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def merge(arr: List[int], start: int, middle: int, end: int) -> None:
            left, right = arr[start: middle + 1], arr[middle + 1: end + 1]
            i, j, k = 0, 0, start

            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    arr[k], i = left[i], i + 1
                else:
                    arr[k], j = right[j], j + 1
                k += 1

            while i < len(left):
                arr[k], i, k = left[i], i + 1, k + 1
            
            while j < len(right):
                arr[k], j, k = right[j], j + 1, k + 1

        def sort(arr: List[int], start: int, end: int) -> None:
            if end - start + 1 <= 1:
                return
            
            middle = (start + end) // 2

            sort(arr, start, middle)
            sort(arr, middle + 1, end)

            merge(arr, start, middle, end)

        copy = nums.copy()
        sort(copy, 0, len(copy) - 1)
        return copy
            


             

