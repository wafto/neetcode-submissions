class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {n: set() for n in range(9)}
        cols = {n: set() for n in range(9)}
        boxes = {n: set() for n in range(9)}

        for r in range(9):
            for c in range(9):
                cell = board[r][c]
                
                if cell == '.':
                    continue
                
                b = (c // 3) + (r // 3) * 3
                if cell in rows[r] or cell in cols[c] or cell in boxes[b]:
                    return False

                rows[r].add(cell)
                cols[c].add(cell)
                boxes[b].add(cell)

        return True

                

