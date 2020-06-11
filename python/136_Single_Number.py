from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        l = []

        for i in nums:
            if i not in l:
                l.append(i)
            else:
                l.remove(i)
        
        return l[0]


if __name__ == "__main__":
    # lists = [2, 2, 1]
    lists = [4, 1, 2, 1, 2]
    # lists = [3,2,2]
    ret = Solution().singleNumber(lists)
    print(ret)