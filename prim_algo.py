class Solution:
    def __init__(self, N, edges):

       self.edges = edges
       self.N = N


    def convert_edges_graph(self, N, edges):
        L = [{} for _ in range(N)]
        for i in edges:
            idx = i[0]
            node = i[1]
            weight = i[2]
            L[idx][node] = weight
        return L

    def closest_node(self, costs):

        """ find the nearest node from the MST
        Note that costs is a dictionary consisting
        of nodes as keys and values as distance from MST """

        min_dist= 9999
        #print(costs,visited)
        for k in costs.keys():
            if costs[k] < min_dist:
                min_dist = costs[k]
                nearest_node = k
                #print(node)
        if min_dist==9999:
            return min_dist
        return nearest_node


    def prim(self, N, edges):
        #define graph as list of dictionaries.
        grid = self.convert_edges_graph(N, edges)
        costs = {k: float('inf') for k in range(N)}

        source = 0
        parent = {k:source for k in grid[source].keys()}

        costs[source]=0
        S=set()

        while len(S) < N:
            node = self.closest_node(costs)
            if node==9999:
                break
            S.add(node)
            #print(S)
            dictnew = grid[node]
            del costs[node]
            #print(costs)

            # iterate over the neighbors of the nearest node
            for k in dictnew.keys():
                if k not in S:
                    new_cost = dictnew[k]
                    if new_cost < costs[k]:
                        costs[k] = new_cost
                        parent[k] = node
        res=0
        for k,v in parent.items():
            res+=grid[v][k]


        return parent,res


obj = Solution(4,[(0,1,5),(0,2,8),(1,0,5),(1,2,10),(1,3,15),(2,0,8),(2,1,10),(2,3,20),(3,1,15),(3,2,20)])
result,resnew = obj.prim(4,[(0,1,5),(0,2,8),(1,0,5),(1,2,10),(1,3,15),(2,0,8),(2,1,10),(2,3,20),(3,1,15),(3,2,20)])
