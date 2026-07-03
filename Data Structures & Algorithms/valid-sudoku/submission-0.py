class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        columns = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                num = board[r][c]

                box = (r//3)*3 + (c//3)

                if num in rows[r] or num in columns[c] or num in boxes[box]:

                    return False

                rows[r].add(num)
                columns[c].add(num)
                boxes[box].add(num)
        return True