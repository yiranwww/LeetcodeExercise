# 743
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {i: [] for i in range(1, n+1)}
        
        for u, v, w in times:
            adj[u].append((v, w)) # u is the source, v is the goal. w is the weight
        pq = [(0, k)] # (current time, current node)
        network = {i: float('inf') for i in range(1, n+1)}
        network[k] = 0

        while pq:
            cur_time, cur_node = heapq.heappop(pq)

            for new_cur, weight in adj[cur_node]:
                new_time = cur_time + weight
                if new_time < network[new_cur]:
                    network[new_cur] = new_time
                    heapq.heappush(pq, (new_time, new_cur))
        
        max_time = max(network.values())
        return max_time if max_time != float('inf') else -1



# 787. Cheapest Flights Within K Stops
from collections import defaultdict
import heapq
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        for fro, to, prc in flights:
            adj[fro].append((to, prc))
        
        heap = [(0, src, 0)]
        best = dict()
        while heap:
            cost, node, flights_used = heapq.heappop(heap)
            if node == dst:
                return cost
            if flights_used > k:
                continue
            for nei, price in adj[node]:
                new_cost = price + cost
                if new_cost < best.get((nei, flights_used +1), float('inf')):
                    best[(nei, flights_used +1)] = new_cost
                    heapq.heappush(heap, (new_cost, nei, flights_used + 1))
        return -1
