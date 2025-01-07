class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        def dfs(node):
            colors[node] = 0
            que = [node]
            while que:
                node = que.pop(0)
                for n in graph[node]:
                    if colors[n] == -1:
                        colors[n] = 1-colors[node]
                        que.append(n)
                    elif colors[n] == colors[node]:
                        return False
            return True
        colors = [-1]*len(graph)
        for g in range(len(graph)):
            if colors[g] == -1:
                if not dfs(g):
                    return False
        return True 

        