class Solution:
    def __init__(self, N, edges,source):

       self.edges = edges
       self.N = N
       self.source=source


    def bellman(self):
        """ Bellman Forda algorithm helps to find shortest path in a DAG
        with positive as well as negative weights"""
        ctr = self.N-1
        arr=[-1]*self.N
        #print(self.N)
        costs={k:float('inf') for k in range(self.N)}
        costs[self.source]=0
        #parent = {0:0}
        for j in range(ctr):
            for k in self.edges:
                if costs[k[1]]>costs[k[0]] + k[2]:
                    costs[k[1]] = costs[k[0]] + k[2]
            #print(costs)
        for j in costs.keys():
            if costs[j]!=float('inf'):
                arr[j]=costs[j]
        return arr
obj=Solution(5,[[0, 4, 2], [1,3, 3], [1, 0, 4], [2, 4, 4], [2, 1, 0], [3, 2, 1], [3, 4, 2], [4, 1, 5]],1)
result = obj.bellman()