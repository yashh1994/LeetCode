import heapq
from typing import List, Dict, Tuple

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj_list: Dict[int, List[Tuple[int, float]]] = {i: [] for i in range(n)}
        for i, (u, v) in enumerate(edges):
            adj_list[u].append((v, succProb[i]))
            adj_list[v].append((u, succProb[i]))

        pro = [0.0] * n
        pro[start_node] = 1.0
        p_que = [(-1.0, start_node)]
        
        while p_que:
            cur_pro, cur_n = heapq.heappop(p_que)
            cur_pro = -cur_pro
            
            if cur_n == end_node:
                return cur_pro

            if cur_pro < pro[cur_n]:
                continue

            for neighbor, edge_prob in adj_list[cur_n]:
                new_prob = cur_pro * edge_prob
                if new_prob > pro[neighbor]:
                    pro[neighbor] = new_prob
                    heapq.heappush(p_que, (-new_prob, neighbor))
        
        return pro[end_node]