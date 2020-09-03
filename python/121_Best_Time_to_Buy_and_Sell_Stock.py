"""
Example 1:
Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.

Example 2:
Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
"""

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        result = []
        min_val = max_val = prices[0]

        for i in prices:
            if i < min_val:
                min_val = max_val = i
            elif max_val < i:
                max_val = i

            result.append(max_val - min_val)

        return max(result)


if __name__ == "__main__":
    # val = [7,1,5,3,6,4]
    val = [2, 4, 1]
    ret = Solution().maxProfit(val)
    print(ret)
