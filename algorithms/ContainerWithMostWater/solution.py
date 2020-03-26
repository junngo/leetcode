'''
Given n non-negative integers a1, a2, ..., an , where each represents 
a point at coordinate (i, ai). n vertical lines are drawn such that
the two endpoints of line i is at (i, ai) and (i, 0). Find two lines,
which together with x-axis forms a container, such that 
the container contains the most water.

Note: You may not slant the container and n is at least 2.
'''


from typing import List

class Solution:
    def maxArea1(self, height: List[int]) -> int:
        max_num = 0
        ret_num = 0

        for idx_i, val_i in enumerate(height):
            for idx_j, val_j in enumerate(height[idx_i+1:]):
                x_axis = idx_j+1

                if val_i < val_j:
                    max_num = val_i * x_axis
                else:
                    max_num = val_j * x_axis

                if ret_num < max_num:
                    ret_num = max_num

        return ret_num

    def maxArea2(self, height: List[int]) -> int:
        max_area = 0
        i = 0
        j = len(height) - 1

        while i < j:
            max_area = max(max_area, min(height[i], height[j]) * (j - i))

            if height[i] < height[j]:
                i += 1
            else:
                j -= 1

        return max_area

if __name__ =='__main__':
    water = Solution().maxArea2([1,8,6,2,5,4,8,3,7])
    print(water)
