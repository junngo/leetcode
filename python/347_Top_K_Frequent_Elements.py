"""
Given a non-empty array of integers, return the k most frequent elements.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]
"""

import collections
import heapq
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = collections.Counter(nums)
        freqs_heap = []

        for f in freqs:
            heapq.heappush(freqs_heap, (-freqs[f], f))

        result = list()
        for _ in range(k):
            result.append(heapq.heappop(freqs_heap)[1])

        return result


if __name__ == "__main__":
    nums = [1,1,1,2,2,3]
    k = 2
    ret = Solution().topKFrequent(nums, k)
    print(ret)
