"""
Problem: Valid Sudoku
Link: neetcode.io/problems/valid-sudoku/question

You are given sudoku board, check if it's valid.
* Board can be unsolvable.
* Board doesn't have to be fully filled in.
"""

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = {"rows": [set() for _ in range(9)],
        "cols": [set() for _ in range(9)],
        "boxes": [set() for _ in range(9)],}

        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num == ".": continue
                seen_row = seen["rows"][i]
                seen_col = seen["cols"][j]
                seen_box = seen["boxes"][(i // 3) * 3 + j // 3]

                if num in seen_row or num in seen_col or num in seen_box:
                    return False

                seen_row.add(num)
                seen_col.add(num)
                seen_box.add(num)

        return True
