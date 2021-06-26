"""
Example 1:
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
"""

class Solution:
    dp = collections.defaultdict(int)
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1

        if n == 2:
            return 2

        if self.dp[n]:
            return self.dp[n]

        self.dp[n] = self.climbStairs(n-1) + self.climbStairs(n-2)

        return self.dp[n]

if __name__ == "__main__":
    result = Solution().climbStairs(5)
    print(result)