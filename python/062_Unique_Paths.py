"""
Example 1:
Input: m = 3, n = 7
Output: 28

Example 2:
Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down

Example 3:
Input: m = 7, n = 3
Output: 28

Example 4:
Input: m = 3, n = 3
Output: 6
"""

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def dfs(m,n):
            if m < 0 or n < 0:
                return 0
            if m == 0 and n == 0:
                return 1

            return dfs(m-1, n) + dfs(m, n-1)

        return dfs(m-1, n-1)


if __name__ == "__main__":
    m = 3
    n = 7
    ret = Solution().uniquePaths(m, n)

    print(ret)
