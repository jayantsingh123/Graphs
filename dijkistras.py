class Solution:
    def __init__(self, N, graph):

       self.graph = graph
       self.N = N


    def convert_edges_graph(self, N, edges):
        """
             in this function we convert edges of wighted graph
               to a list of dictionaries
             N is number of nodes from 0 to N-1
             for example, we have [[0, 1, 2], [0, 3, 5]]
             i.e. there is a directed edge from 0 to 1 with weight 2 and
             directed edge from 0 to 3 with weight 5
             output will be [{1:2, 3:5}] at index 0 we will have a dictionary
              with keys as nodes and values as weights   """
        L=[{} for _ in range(N)]
        for i in edges:
            idx = i[0]
            node = i[1]
            weight = i[2]
            L[idx][node] = weight
        return L



    def closest_node(self, costs, visited):

        """ find the nearest node from the source
        Note that costs is a dictionary consisting
        of nodes as keys and values as distance from source """

        min_dist= 9999
        #print(costs,visited)
        for k in costs.keys():
            if not visited[k] and costs[k] < min_dist:
                min_dist = costs[k]
                nearest_node = k
                #print(node)
        if min_dist==9999:
            return min_dist
        return nearest_node


    def dijkistras(self, N, edges, source):
        #define graph as list of dictionaries.
        grid = self.convert_edges_graph(N, edges)
       # print(grid)
        L=[] #define a list to store the distance from source to all nodes numbered from 0 to N-1
        # initialize costs with distances for immediate neighbors of the source
        # initialize parent with source and its neighbors

        parent = {k:source for k in grid[source].keys()}
        costs = {k:v for k,v in grid[source].items()}
        costs[source]=0
        q = [source]
        visited = [False]*N
        visited[source]=True
        while len(q)>0:
            elem = q.pop(0)
            node = self.closest_node(costs, visited)
            if node==9999:
                break
            visited[node] = True
            dictnew = grid[node]
            #print(costs)

            # iterate over the neighbors of the nearest node
            for k in dictnew.keys():
                new_cost = costs[node] + dictnew[k]

                #if the new distance is less than original value, update the cost/distance.
                if costs.get(k)==None or new_cost < costs[k]:
                    costs[k] = new_cost
                    parent[k] = node
            q.append(node)
        for k in range(N):
            #if some node is not reachable from source, put -1 for distance.
            if costs.get(k) == None:
                L.append(-1)
            else:
                L.append(costs[k])
        return L

obj=Solution(6, [[0, 1, 2], [0, 2, 3], [1, 3, 1], [2, 3, 2], [4, 5, 4], [5, 4, 3]])
result = obj.dijkistras(6, [[0, 1, 2], [0, 2, 3], [1, 3, 1], [2, 3, 2], [4, 5, 4], [5, 4, 3]],2)






