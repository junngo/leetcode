'''
Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.

Input:
[
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: true

'''
from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        self.check = {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0,
                      "6": 0, "7": 0, "8": 0, "9": 0}

        col_len = len(board[0])
        row_len = len(board)

        # row check
        for i in range(0, row_len):
            for j in range(0, col_len):
                key = board[i][j]
                if key !=  ".":
                    self.check[key] += 1
                
            for k in self.check:
                if 1 < self.check[k]:
                    return False

            self.init_check(self.check)

        # column check
        for i in range(0, col_len):
            for j in range(0, row_len):
                key = board[j][i]
                if key !=  ".":
                    self.check[key] += 1
                
            for k in self.check:
                if 1 < self.check[k]:
                    return False

            self.init_check(self.check)

        # 3x3 sub-boxes
        for i in range(0, row_len, 3):
            for j in range(0, col_len, 3):
                self.check_sub_box(i, j, board, self.check)

                for k in self.check:
                    if 1 < self.check[k]:
                        return False

                self.init_check(self.check)

        return True

    def check_sub_box(self, i, j, board, check):
        init_j = j

        for i in range(i, i+3):
            for j in range(j, j+3):
                key = board[i][j]
                if key !=  ".":
                    self.check[key] += 1

            j = init_j

    def init_check(self, check):
        for i in check:
            check[i] = 0


if __name__ == "__main__":
    board = [
        ["5","3",".",".","7",".",".",".","."],
        ["6","7",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    
    ret = Solution().isValidSudoku(board)
    print(ret)
