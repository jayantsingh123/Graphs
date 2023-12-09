class Solution:
    def __init__(self, grid):
        self.grid = grid

    def is_valid_cell(self, newrow, newcol, nrows,ncols):
        return 0<=newrow<nrows and 0<=newcol<ncols

    def traverse_neighbors_cost(self, grid, curr_row, curr_col,costs,parent,newrow,newcol):
        #print(costs,grid,curr_row,curr_col,newcol,newrow,)
        new_cost = costs[(curr_row,curr_col)] + grid[newrow][newcol]
        if costs.get((newrow,newcol)) == None or new_cost < costs[(newrow,newcol)]:
            costs[(newrow,newcol)] = new_cost
            parent[(newrow,newcol)] = (curr_row,curr_col)

        return




    def closest_node(self, costs, visited):
        min_dist = 9999
        for k in costs.keys():
            if not visited[k[0]][k[1]] and costs[k] < min_dist:
                min_dist = costs[k]
                nearest_node = k
        if min_dist == 9999:
            return ()
        return nearest_node




    def dijkistras(self, grid):
        source = (0,0)
        nrows,ncols = len(grid),len(grid[0])
        target = (nrows-1,ncols-1)
        visited = [[False] * ncols for _ in range(nrows)]

        curr_row,curr_col=0,0
        costs = {source: grid[curr_row][curr_col]}
        parent = {source:source}
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        for i in range(len(dx)):
            newrow = curr_row + dy[i]
            newcol = curr_col + dx[i]
            if self.is_valid_cell(newrow, newcol, nrows, ncols):
                self.traverse_neighbors_cost(grid, curr_row, curr_col,costs,parent,newrow,newcol)
        q = [source]
        visited[curr_row][curr_col]=True
        while len(q)>0:
            elem = q.pop(0)
            nearest_idx = self.closest_node(costs, visited)
            if len(nearest_idx)==0:
                break
            curr_row, curr_col = nearest_idx[0] , nearest_idx[1]
            visited[curr_row][curr_col] = True
            for i in range(len(dx)):
                newrow = curr_row + dy[i]
                newcol = curr_col + dx[i]
                if self.is_valid_cell(newrow, newcol, nrows, ncols):
                    self.traverse_neighbors_cost(grid, curr_row, curr_col, costs, parent, newrow, newcol)
                if (newrow,newcol)==target:
                    print(costs, newrow,newcol,grid[newrow][newcol],target)
                    return costs[(newrow,newcol)]
            q.append((curr_row,curr_col))
        return

obj = Solution([[9, 4, 9, 9], [1, 7, 6, 4], [1, 3, 3, 7], [1, 2, 2, 10]])
result = obj.dijkistras([[9, 4, 9, 9], [1, 7, 6, 4], [1, 3, 3, 7], [1, 2, 2, 10]])