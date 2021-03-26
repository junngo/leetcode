"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
"""

from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def dfs(leftRemain, rightRemain, path, res):
            if leftRemain > rightRemain or leftRemain < 0 or rightRemain < 0:
                return  # backtracking

            if leftRemain == 0 and rightRemain == 0:
                res.append(path)
                return 

            dfs(leftRemain-1, rightRemain, path+"(", res)
            dfs(leftRemain, rightRemain-1, path+")", res)

        dfs(n, n, "", result)

        return result


if __name__ == '__main__':
    n = 3
    result = Solution().generateParenthesis(n)
    print(result)
