class Solution:

    def __init__(self, grid):
        self.grid = grid

    def dfs_cycle_detect(self, grid, node, visited, parent):
        visited[node]=True
        for j in grid[node]:
            if visited[j]==False:
                parent[j] = node
                return self.dfs_cycle_detect(grid, j, visited, parent)
            else:
                if j!=parent[node]:
                    # while traversing the neighbors, if there is an already visited node
                    # which is not the parent, means we have a cycle.
                      return True
        return False

    def dfs_cycle_main(self, grid):
        node = 0
        visited = [False] * len(grid)
        dnew={node:0}
        res = self.dfs_cycle_detect(grid, node, visited, dnew)
        return res

obj = Solution([[1], [0, 2, 3, 4], [1, 3], [2, 1], [1]])
result = obj.dfs_cycle_main([[1], [0, 2, 3, 4], [1, 3], [2, 1], [1]])