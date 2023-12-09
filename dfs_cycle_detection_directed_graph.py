class Solution:

    def __init__(self, grid):
        self.grid = grid


    def dfs_cycle_detect_directed(self, grid, node, visited, rec_stack):
        visited[node] = True
        rec_stack[node] = True
        for j in grid[node]:
            # if neighbor j is not visited, do regular dfs call
            # Add-on, if the dfs call detects a loop, then return True
            if visited[j] == False and self.dfs_cycle_detect_directed(grid, j, visited, rec_stack):
                return True
            # if neighbor j is visited, but it is in the recursive stack, means there is a back edge
            # from node to j, hence loop exists
            else:
                if rec_stack[j] == True:
                    return True
       # remove the function call from recursive stack
        rec_stack[node] = False
        return False


    def dfs_cycle(self, grid):
        v = len(grid)
    # define list to keep track of visited nodes
        visited = [False] * v
    # define list to keep track of recursive calls
        rec_stack = [False] * v
        for i in range(v):
            # iterate through unvisited nodes
            if visited[i]==False:
               res = self.dfs_cycle_detect_directed(grid, i, visited, rec_stack)
               if res == True:
                   return True
        return False

obj = Solution([[4],[5],[3],[5],[1],[]])
result = obj.dfs_cycle([[4],[5],[3],[5],[1],[]])