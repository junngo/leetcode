from typing import List

class Solution:
    def countSmaller_bf(self, nums: List[int]) -> List[int]:
        result = []
        for idx, val in enumerate(nums):
            cnt = 0
            for num in nums[idx+1:]:
                if num < val:
                    cnt += 1

            result.append(cnt)

        return result

    def countSmaller(self, nums: List[int]) -> List[int]:
        pass


if __name__ == "__main__":
    nums = [5,2,6,1]
    reuslt = Solution().countSmaller(nums)
    print(reuslt)
