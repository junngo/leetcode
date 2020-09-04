"""
Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""

from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        results = []

        def dfs(index: int, path: List):
            results.append(path)

            for i in range(index, len(nums)):
                dfs(i + 1, path + [nums[i]])

        dfs(0, [])
        return results

if __name__ == "__main__":
    input = [1, 2, 3]
    ret = Solution().subsets(input)
    print(ret)
