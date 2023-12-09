class Solution:
    def __init__(self, N, edges):

       self.edges = edges
       self.N = N

    def convert_edges_graph(self, N, edges):
        grid = [{} for _ in range(N)]
        actual_flow = [{} for _ in range(N)]
        residue = [{} for _ in range(N)]
        for i in edges:
            idx = i[0]
            node = i[1]
            weight = i[2]
            grid[idx][node] = weight
            # for backward flow swap idx and node
            grid[node][idx] = weight
            actual_flow[idx][node] = 0
            actual_flow[node][idx]=0
            residue[idx][node] = grid[idx][node] - actual_flow[idx][node]
            residue[node][idx] = 0
        return grid, actual_flow, residue

    def change_residual_capacity(self, minimum_residue, residue, L1):
        """ e.g. L1=[5,4,2,1,0] is a path then it is  same as 0 -> 1 -> 2 -> 4 -> 5"""
        while len(L1)>=2:
            element = L1.pop()
            #decrease residue for forward path
            residue[element][L1[-1]] -= minimum_residue
            #increase residue for backward path
            residue[L1[-1]][element] += minimum_residue


        return residue


    def bfs(self, grid, visited, residue, parent_dict):
       source = 0
       q=[]
       q.append(source)
       visited[source]=True
       #parent={}
       while len(q)>0:
           elem = q.pop(0)
           dictnew = grid[elem]
           for j in dictnew.keys():
               if not visited[j] and residue[elem][j]>0:
                   visited[j]=True
                   q.append(j)
                   parent_dict[j]=elem
                   if j==len(grid)-1:
                       return True
       return False

    def construct_path(self, parent, key, L):

        if key==0:
            L.append(0)
            return L
        L.append(key)
        self.construct_path(parent, parent[key],L)

    def minimum_residue(self, L, residue):
        # given a path find the bottleneck, i.e. minimum residue
        min_val=99999
        while len(L)>=2:
            elem = L.pop()
            min_val = min(residue[elem][L[-1]],min_val)
        return min_val

    def mainfn(self, N, edges):
        # initialize, grid, actual flow as well as residual capacity
        grid, actual_flow, residue = self.convert_edges_graph(N, edges)
        visited=[False] * N
        source_dict = residue[0]
        flow=0
        parent_dict={}
        # how to decide when to stop looking for paths
        # as long as bfs is giving us augmented paths
        while self.bfs(grid, visited, residue, parent_dict):
            L=[]
            self.construct_path(parent_dict, N-1, L)
            # since L is mutable
            L1=L.copy()
            minimum_residue = self.minimum_residue(L, residue)
            #decrease the residual capacity on this path by minimum_residue amount
            self.change_residual_capacity(minimum_residue, residue, L1)
            #reinitialize visited for the new path
            visited = [False] * N
            #increase the flow with each path by minimum_residue amount
            flow += minimum_residue
            parent_dict={}

        return  flow

obj = Solution(6, [[0,1,10],[0,2,10],[1,3,4],[1,2,2],[1,4,8],[2,4,9],[4,3,6],[3,5,10],[4,5,10]])
res = obj.mainfn(6, [[0,1,10],[0,2,10],[1,3,4],[1,2,2],[1,4,8],[2,4,9],[4,3,6],[3,5,10],[4,5,10]])