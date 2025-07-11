class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(i):
            for j in range(len(isConnected)):
                if isConnected[i][j] and not visited[j]:
                    visited[j] = True
                    dfs(j)
        provinces = 0
        visited = [False]*len(isConnected)
        for i in range(len(isConnected)):
            if not visited[i]:
                provinces +=1
                visited[i] = True
                dfs(i)
        return provinces

        
