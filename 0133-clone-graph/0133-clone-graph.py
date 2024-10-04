# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from typing import Optional

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        ans = Node(node.val)
        q1 = []
        q2 = []
        q1.append(node)
        q2.append(ans)
        visited = {}
        visited[node] = ans 
        
        while q1:
            cur = q1.pop(0)
            new_node = visited[cur] 
            
            for neighbor in cur.neighbors:
                if neighbor not in visited:
                    temp = Node(neighbor.val)
                    visited[neighbor] = temp  
                    q1.append(neighbor)
                    q2.append(temp)
                
                new_node.neighbors.append(visited[neighbor]) 
        
        return ans
