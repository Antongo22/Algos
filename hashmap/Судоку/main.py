from typing import List
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = set()
        cols = set()
        blocks = set()

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == ".":
                    continue

                lr = len(rows)
                lc = len(cols)
                lb = len(blocks)
                rows.add((i, board[i][j]))
                cols.add((j, board[i][j]))
                blocks.add( (i // 3 * 3 + j //3, board[i][j]) )        

                if lr == len(rows) or lc == len(cols) or lb == len(blocks):
                    return False

        return True
        