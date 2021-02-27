"""
Example 1:
Input: [3,2,1,5,6,4] and k = 2
Output: 5

Example 2:
Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4
"""
from typing import List
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = list()
        for n in nums:
            heapq.heappush(heap, -n)
        
        for _ in range(k-1):
            print(heapq. heappop(heap))
        

        return -heapq.heappop(heap)


if __name__ == "__main__":
    nums = [3,2,1,5,6,4]
    k = 2
    result = Solution().findKthLargest(nums, k)
    print(result)
