class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row = len(matrix)
        col = len(matrix[0])
        z = []
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    z.append((i,j))
        for r,c in z:
            for j in range(col):
                matrix[r][j] = 0
            for i in range(row):
                matrix[i][c] = 0
        