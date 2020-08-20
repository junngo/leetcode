'''
Given a list of daily temperatures T, return a list such that, for each day in the input, tells you how many days you would have to wait until a warmer temperature. If there is no future day for which this is possible, put 0 instead.

For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73], your output should be [1, 1, 4, 2, 1, 1, 0, 0].

'''

from typing import List

class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack = []
        answer = [0] * len(T)

        for i, cur in enumerate(T):
            while stack and cur > T[stack[-1]]:
                last = stack.pop()
                answer[last] = i - last
            stack.append(i)

        return answer


if __name__ == "__main__":
    t = [73, 74, 75, 71, 69, 72, 76, 73]
    ret = Solution().dailyTemperatures(t)
    # print(ret)

