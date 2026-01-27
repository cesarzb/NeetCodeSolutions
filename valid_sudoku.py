"""
Problem: Valid Sudoku
Link: neetcode.io/problems/valid-sudoku/question

You are given sudoku board, check if it's valid.
* Board can be unsolvable.
* Board doesn't have to be fully filled in.
"""

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for i, row in enumerate(board):
            print(i)
            for j, num in enumerate(row):
                if num == ".": continue
                if num in rows[i]: return False
                if num in cols[j]: return False
                box_number = (i // 3) * 3 + j // 3
                if num in boxes[box_number]: return False
                rows[i].add(num)
                cols[j].add(num)
                boxes[box_number].add(num)
        
        return True

