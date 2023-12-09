class Solution:
   def __init__(self, matrix):
        self.matrix = matrix

   def convert_matrix_grid(self,matrix):
       from collections import defaultdict
       """ in this method we are defining the job applicants as 
           well as jobs to numbers, so that we can use the logic developed
           in ford fulkerson algorithm """
       nrows = len(matrix)
       ncols = len(matrix[0])
       columns_hash = defaultdict(int)
       columns_hash[0]=nrows+1
       # define hash map for column indices
       for j in range(1,ncols):
           columns_hash[j] = columns_hash[j-1]+1

       grid = [{} for _ in range(nrows+1)]
       actual_flow = [{} for _ in range(nrows+1)]
       residue = [{} for _ in range(nrows+1)]
       # define grid for matching applicants to jobs
       for i in range(nrows):
           for j in range(ncols):
               grid[i+1][columns_hash[j]] = matrix[i][j]
               actual_flow[i+1][columns_hash[j]] = 0
               residue[i+1][columns_hash[j]] = grid[i+1][columns_hash[j]] - actual_flow[i+1][columns_hash[j]]
       # add dictionary to attach source (defined as index 0) to applicants.
       dnew = {k:1 for k in range(1, nrows+1)}
       grid[0]=dnew
       residue[0]=dnew
       # add edges from jobs to the sink, of weight 1
       for  k in columns_hash.values():
           grid.insert(k,{max(columns_hash.values())+1:1})
           residue.insert(k, {max(columns_hash.values()) + 1: 1})

       return grid,actual_flow,residue

   def change_residual_capacity(self, minimum_residue, residue, L1):
       """ e.g. L1=[5,4,2,1,0] is a path then it is  same as 0 -> 1 -> 2 -> 4 -> 5"""
       while len(L1) >= 2:
           element = L1.pop()
           # decrease residue for forward path
           # for example residue on the path between 0 and 1 is reduced by minimum residue
           residue[element][L1[-1]] -= minimum_residue

       return residue

   def bfs(self, grid, visited, residue, parent_dict):
       source = 0
       q = []
       q.append(source)
       visited[source] = True
       # parent={}
       while len(q) > 0:
           elem = q.pop(0)
           dictnew = grid[elem]
           #print(grid,visited,residue)
           for j in dictnew.keys():
               print(j,elem,residue,visited)
               if not visited[j] and residue[elem][j] > 0:
                   visited[j] = True
                   q.append(j)
                   parent_dict[j] = elem
                   if j == len(grid):
                       return True
       return False

   def construct_path(self, parent, key, L):

       """ given the parent dictionary, we define the path from source to sink"""

       if key == 0:
           L.append(0)
           return L
       L.append(key)
       self.construct_path(parent, parent[key], L)

   def minimum_residue(self, L, residue):
       # given a path find the bottleneck, i.e. minimum residue
       min_val = 99999
       while len(L) >= 2:
           elem = L.pop()
           min_val = min(residue[elem][L[-1]], min_val)
       return min_val

   def mainfn(self, matrix):
       # initialize, grid, actual flow as well as residual capacity
       grid, actual_flow, residue = self.convert_matrix_grid(matrix)
       N=len(grid)+1
       visited = [False] * N
       source_dict = residue[0]
       flow = 0
       parent_dict = {}
       # how to decide when to stop looking for paths
       # as long as bfs is giving us augmented paths
       while self.bfs(grid, visited, residue, parent_dict):
           L = []
           self.construct_path(parent_dict, N - 1, L)
           # since L is mutable, copying will assure that L1 doesn't change if L changes
           L1 = L.copy()
           minimum_residue = self.minimum_residue(L, residue)
           # decrease the residual capacity on this path by minimum_residue amount
           self.change_residual_capacity(minimum_residue, residue, L1)
           # reinitialize visited for the new path
           visited = [False] * N
           # increase the flow with each path by minimum_residue amount
           flow += minimum_residue
           parent_dict = {}

       return flow


obj = Solution([[1,0],[0,1]])
res = obj.mainfn([[1,0],[0,1]])