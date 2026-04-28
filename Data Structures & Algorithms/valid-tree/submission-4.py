class Solution:
  def validTree(self, n: int, edges: List[List[int]]) -> bool:
    if len(edges) > n-1:
        return False
    if n == 1: return True
    nodes = {}
    for edge in edges:
        if edge[0] in nodes:
            nodes[edge[0]].append(edge[1])
        else:
            nodes[edge[0]] = [edge[1]]
        if edge[1] in nodes:
            nodes[edge[1]].append(edge[0])
        else:
            nodes[edge[1]] = [edge[0]]

    print(nodes)
    visited = set()
    def dfs(node, parent):
        if node in visited:
            return False
        visited.add(node)
        for neighbor in nodes[node]:
            if neighbor == parent:
                continue
            if not dfs(neighbor, node):
                return False
        return True
    return dfs(0, -1) and len(visited) == n

