'''
Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.
The same repeated number may be chosen from candidates unlimited number of times.

Example 1:
Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]

Example 2:
Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
'''

from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()

        def dfs(target, index, path):
            if target < 0:
                return  # backtracking
            if target == 0:
                result.append(path)
                return
            for i in range(index, len(candidates)):
                dfs(target-candidates[i], i, path+[candidates[i]])

        dfs(target, 0, [])

        return result

if __name__ == "__main__":
    candidates = [2,3,6,7]
    target = 7

    ret = Solution().combinationSum(candidates, target)
    print(ret)
