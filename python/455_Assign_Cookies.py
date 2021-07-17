from typing import List

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        child = cookie = 0
        while child < len(g) and cookie < len(s):
            if s[cookie] >= g[child]:
                child += 1
            cookie += 1
        
        return child

if __name__ == "__main__":
    g = [1, 2, 3]
    s = [1, 1]
    # [10,9,8,7]
    # [5,6,7,8]

    result = Solution().findContentChildren(g, s)
    print(result)
