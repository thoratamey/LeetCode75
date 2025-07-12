class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        edges = {(a, b) for a, b in connections}
        neighbours = {city: [] for city in range(n)}
        changes = 0
        visit = set()

        for a, b in connections:
            neighbours[a].append(b)
            neighbours[b].append(a)

        def dfs(city):
            nonlocal changes
            for neighbor in neighbours[city]:
                if neighbor in visit:
                    continue
            
                if (neighbor, city) not in edges:
                    changes += 1
                visit.add(neighbor)
                dfs(neighbor)

        visit.add(0)
        dfs(0)
        return changes
