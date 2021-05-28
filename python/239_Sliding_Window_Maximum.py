import collections
from typing import List

class Solution:
    def maxSlidingWindow_brute_force(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return nums
        
        r = []
        for i in range(len(nums) - k + 1):
            r.append(max(nums[i:i+k]))

        return r

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        results = []
        window = collections.deque()
        current_max = float('-inf')
        for i, v in enumerate(nums):
            window.append(v)
            print(v, window)
            if i < k - 1:
                continue

            if current_max == float('-inf'):
                current_max = max(window)
            elif v > current_max:
                current_max = v

            results.append(current_max)

            if current_max == window.popleft():
                current_max = float('-inf')

        return results


if __name__ == "__main__":
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    result = Solution().maxSlidingWindow(nums, k)
    for r in result:
        print(r)
