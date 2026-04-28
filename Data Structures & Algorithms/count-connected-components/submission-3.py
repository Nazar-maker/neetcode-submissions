class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        nodes = [[] for _ in range(n)]
        for u, v in edges:
            nodes[u].append(v)
            nodes[v].append(u)

        # for edge in edges:
        #     if edge[0] in nodes:
        #         nodes[edge[0]].append(edge[1])
        #     else:
        #         nodes[edge[0]] = [edge[1]]
        # print(nodes)
        def dfs(node):
            for neighbor in nodes[node]:
                if not visit[neighbor]:
                    visit[neighbor] = True
                    dfs(neighbor)

        visit = [False]*n
        count = 0
        for i in range(n):
            if not visit[i]:
                visit[i] = True
                dfs(i)
                count += 1
        return count
        
        