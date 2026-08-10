class Solution:
    def countBits(self, n: int) -> List[int]:
        # 0: 0000 0000 -> 0 = 0
        # 1: 0000 0001 -> 1 = 1 + memo[n - 1]
        # 2: 0000 0010 -> 1 = 1 + memo[n - 2]
        # 3: 0000 0011 -> 2 = 1 + memo[n - 2]
        # 4: 0000 0100 -> 1 = 1 + memo[n - 4]
        # 5: 0000 0101 -> 2 = 1 + memo[n - 4]
        # 6: 0000 0110 -> 2 = 1 + memo[n - 4]
        # 7: 0000 0111 -> 3 = 1 + memo[n - 4]
        # 8: 0000 1000 -> 1 = 1 + memo[n - 8]
        memo = [0] * (n + 1)
        offset = 1
        for i in range(1, n + 1):
            if offset * 2 == i:
                offset = i
            memo[i] = 1 + memo[i - offset]
        return memo
