class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def merge(data: List[int], start: int, end: int) -> None:
            if end - start + 1 <= 1:
                return

            middle = (end + start) // 2
            merge(data, start, middle)
            merge(data, middle + 1, end)

            helper(data, start, middle, end)
        
        def helper(data: List[int], start: int, middle: int, end: int) -> None:
            left = data[start: middle + 1]
            right = data[middle + 1: end + 1]

            i, j, k = 0, 0, start
            
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    data[k] = left[i]
                    i += 1
                else:
                    data[k] = right[j]
                    j += 1
                k += 1

            while i < len(left):
                data[k] = left[i]
                i, k = i + 1, k + 1

            while j < len(right):
                data[k] = right[j]
                j, k = j + 1, k + 1

        data = nums.copy()
        merge(data, 0, len(data) - 1)
        return data
            

