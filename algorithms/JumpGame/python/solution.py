from typing import List

class Solution:
    def canJump(self, nums:List[int]) -> bool:
        length = len(nums)
        reach = 0

        for i in range(length):
            if i > reach:
                return False

            if i + nums[i] > reach:
                reach = i + nums[i]

        return True


if __name__ == "__main__":
    my_list = [3, 6, 0, 0, 1]
    ret = Solution().canJump(my_list)
    print(ret)
