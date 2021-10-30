import collections
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = collections.defaultdict(int)
        for num in nums:
            if counts[num] == 0:
                counts[num] = nums.count(num)

            if counts[num] > len(nums) // 2:
                return num

if __name__ == "__main__":
    nums = [2, 2, 1, 1, 1, 2, 2]
    result = Solution().majorityElement(nums)
    print(result)
