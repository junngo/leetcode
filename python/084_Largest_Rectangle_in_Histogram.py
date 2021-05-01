"""
Input: heights = [2,1,5,6,2,3]
Output: 10

Input: heights = [2,4]
Output: 4
"""

from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        stack = [-1]
        ans = 0

        for i in range(len(heights)):
            while heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i - stack[-1] - 1
                ans = max(ans, h * w)

            stack.append(i)

        heights.pop()

        return ans

if __name__ == "__main__":
    heights = [2,1,5,6,2,3]
    result = Solution().largestRectangleArea(heights)
    print(result)
