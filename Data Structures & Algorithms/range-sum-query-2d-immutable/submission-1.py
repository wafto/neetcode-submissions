class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        self.rows, self.cols = len(matrix), len(matrix[0])
        self.ps = [[0] * (self.cols + 1) for _ in range(self.rows + 1)]
        
        for r in range(self.rows):
            ps = 0
            for c in range(self.cols):
                ps += matrix[r][c]
                self.ps[r + 1][c + 1] = ps + self.ps[r][c + 1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        r1, c1, r2, c2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1
        bottom_right = self.ps[r2][c2]
        bottom_left = self.ps[r2][c1 - 1]
        top_right = self.ps[r1 - 1][c2]
        top_left = self.ps[r1 - 1][c1 - 1]

        return bottom_right - bottom_left - top_right + top_left



# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)