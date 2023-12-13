class Solution:

    def __init__(self):
        self.grid = None

    def bfs(self, grid, source, destination, L):
        q=[[source]]
       # L=[]
        while len(q)>0:
            # get the path found so far in FIFO order
            curr_path=q.pop(0)
            # get the last element of that path and traverse its neighbors
            elem = curr_path[-1]
            for j in grid[elem]:
                # make a copy so that curr_path doesn't get changed
                # helps to have different values of temp_path as the neighbor changes for a node, since we want
                # all possible paths
                temp_path=curr_path.copy()
                temp_path.append(j)
                if j==destination:
                    L.append(temp_path)
                else:
                    q.append(temp_path)


        return

    def countpaths(self,grid, source, destination):
        """ get list of all paths from source to destination in directed graph"""
        L=[]
        if len(grid[source])==0:
            return 0
        if source==destination:
            return 1
        self.bfs(grid, source, destination, L)
        return len(L)

if __name__=="__main__":
    obj = Solution()
    res = obj.countpaths([[1,2,4],[3,4],[4],[2],[]], 1, 4)

