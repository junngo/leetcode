"""
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.

Given n, calculate F(n).

Example 1:
Input: n = 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.

Example 2:
Input: n = 3
Output: 2
Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.

Example 3:
Input: n = 4
Output: 3
Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.

"""

import collections

class Solution:
    dp = collections.defaultdict(int)

    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        
        return self.fib(n - 1) + self.fib(n - 2)


    def fib_memoization(self, n: int) -> int:
        if n <= 1:
            return n

        if self.dp[n]:
            return self.dp[n]
        
        self.dp[n] = self.fib_memoization(n - 1) + self.fib_memoization(n - 2)
        return self.dp[n]


    def fib_talulate(self, n: int) -> int:
        self.dp[1] = 1

        for i in range(2, n+1):
            self.dp[i] = self.dp[i - 1] + self.dp[i - 2]

        return self.dp[n]


if __name__ == "__main__":
    num = 8
    result = Solution().fib_talulate(num)
    print(result)
