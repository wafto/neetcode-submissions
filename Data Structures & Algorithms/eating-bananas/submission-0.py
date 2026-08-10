class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        k = right

        while left <= right:
            middle = left + (right - left) // 2
            
            total = 0
            for pile in piles:
                total += math.ceil(float(pile) / middle)

            if total <= h:
                k = middle
                right = middle - 1
            else:
                left = middle + 1

        return k



