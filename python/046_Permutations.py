"""
Given a collection of distinct integers, return all possible permutations.

Example:
Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""

from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(elements: List[int]):
            if len(elements) == 0:
                result.append(prev_elements[:])

            for i in elements:
                next_elements = elements[:]
                next_elements.remove(i)

                prev_elements.append(i)
                dfs(next_elements)
                prev_elements.pop()

        result = []
        prev_elements = []
        dfs(nums)

        return result

if __name__ == "__main__":
    values = [1,2,3]
    ret =   Solution().permute(values)
    print(ret)
