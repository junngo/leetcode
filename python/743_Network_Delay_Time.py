"""
Example 1:
Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
Output: 2

Example 2:
Input: times = [[1,2,1]], n = 2, k = 1
Output: 1

"""

import collections
import heapq
from typing import List

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        
        # 큐변수 [(소요time, 정점)]
        Q = [(0, k)]
        dist = collections.defaultdict(int)

        # 우선순위 큐 최솟value 기준으로 정점까지 최단 경로 삽입
        while Q:
            time, node = heapq.heappop(Q)
            if node not in dist:
                dist[node] = time
                for v, w in graph[node]:
                    alt = time + w
                    heapq.heappush(Q, (alt, v))
        
        # 모든 노드의 최단경로 존재 여부 판별
        if len(dist) == n:
            return max(dist.values())
        
        return -1

if __name__ == "__main__":
    # times = [[2,1,1],[2,3,1],[3,4,1]]
    # n = 4
    # k = 2
    # times = [[1,2,1]]
    n = 8
    k = 3
    times = [[3, 1, 5], [3, 2, 2], [2, 1, 2], [3, 4, 1], [4, 5, 1], [5, 6, 1], [6, 7, 1] ,[7, 8, 1] ,[8, 1, 1]]
    ret = Solution().networkDelayTime(times, n, k)
    print(ret)
