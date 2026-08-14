class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {n: set() for n in range(9)}
        cols = {n: set() for n in range(9)}
        boxes = {n: set() for n in range(9)}

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                b = (r // 3) * 3 + (c // 3)
                if val != '.':
                    if val in rows[r] or val in cols[c] or val in boxes[b]:
                        return False
                    rows[r].add(val)
                    cols[c].add(val)
                    boxes[b].add(val)

        return True
        