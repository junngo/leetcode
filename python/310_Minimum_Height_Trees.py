"""
Input: n = 4, edges = [[1,0],[1,2],[1,3]]
Output: [1]
Explanation: As shown, the height of the tree is 1 when the root is the node with label 1 which is the only MHT.

Input: n = 6, edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
Output: [3,4]
"""

import collections
from typing import List

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 1:
            return [0]

        graph = collections.defaultdict(list)
        for j, i in edges:
            graph[i].append(j)
            graph[j].append(i)
        
        leaves = []
        print(graph)
        for i in range(n + 1):
            if len(graph[i]) == 1:
                leaves.append(i)

        while n > 2:
            n -= len(leaves)
            new_leaves = []
            for leaf in leaves:
                neighbor = graph[leaf].pop()
                graph[neighbor].remove(leaf)

                if len(graph[neighbor]) == 1:
                    new_leaves.append(neighbor)
            
            leaves = new_leaves

        return leaves


if __name__ == "__main__":
    n = 4
    edges = [[1,0],[1,2],[1,3]]
    result = Solution().findMinHeightTrees(n, edges)
    print(result)
