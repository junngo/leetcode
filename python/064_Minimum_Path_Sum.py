from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        col_len = len(grid[0])
        row_len = len(grid)

        for i in range(1, col_len):
            grid[0][i] = grid[0][i-1] + grid[0][i]

        for i in range(1, row_len):
            grid[i][0] = grid[i-1][0] + grid[i][0]

        for i in range(1, row_len):
            for j in range(1, col_len):
                grid[i][j] = min(grid[i-1][j], grid[i][j-1]) + grid[i][j]

        return grid[-1][-1]


if __name__ == '__main__':
    val = [[1,2,5],[3,2,1]]
    # val = [[1,3,1], [1,5,1], [4,2,1]]
    ret = Solution().minPathSum(val)
    print(ret)
