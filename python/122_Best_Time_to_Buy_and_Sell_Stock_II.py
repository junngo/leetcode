from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return sum([
            max(prices[i] - prices[i - 1], 0) for i in range(1, len(prices))
        ])

if __name__ == "__main__":
    my_list = [7,1,5,3,6,4]
    ret = Solution().maxProfit(my_list)
    print(ret)
