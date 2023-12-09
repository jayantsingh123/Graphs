class Solution:
    def __init__(self, graph):
       self.graph = graph



    def graph_transpose(self, graph):
        graph_t = [[] for _ in range(len(graph))]
        for elem in range(len(graph)):
            for j in graph[elem]:
               # revert the edge
               graph_t[j].append(elem)
        return graph_t


    def graph_reverse(self, graph):
        # we'll use this method to reverse the graph if it is arranged as a dictionary
        # with keys and values being alphabets. Unlike numbers, we can't use range functionality here
        graph_reverse = {k:[] for k in graph.keys()}
        for elem in graph.keys():
            for j in graph[elem]:
                graph_reverse[j].append(elem)
        return graph_reverse


    def dfs_graph_help(self, graph, visited, stack, node):
        visited.add(node)
        for j in graph[node]:
            if not j in visited:
                self.dfs_graph_help(graph, visited, stack, j)
        # if all neighbors have been visited add the node to stack
        stack.append(node)
        #print(stack)
        return

    def dfs_graph_reverse(self, graph, visited, node, L1):
       # print(strnew)
        visited.add(node)
        for j in graph[node]:
            if not j in visited:
                self.dfs_graph_reverse(graph, visited, j, L1)
        # if all neighbors have been visited add the node to string
        L1.append(node)
        return


    def dfs_main(self, graph):
        #visited = {'a':False, 'b':False, 'c': False, 'd':False, 'e':False, 'f':False, 'g':False,'h':False, 'i':False, 'j':False, 'k':False}
        stack,L,L1 =[],[],[]

        visited=set()
        #if graph is a dictionary, call graph_reverse
        if type(graph)==dict:
            graph_rev = self.graph_reverse(graph)
        #if graph is a list of lists, call graph_transpose
        if type(graph)==list:
            graph_rev = self.graph_transpose(graph)
       # perform DFS on original graph
        for j in graph.keys():
            if not j in visited:
                self.dfs_graph_help(graph, visited, stack, j)
       # return stack
        visited = set()

        while len(stack)>0:
            elem = stack.pop(-1)
            #print(visited)
            if not elem in visited:
               # print(elem)
                self.dfs_graph_reverse(graph_rev, visited, elem, L1)
               # print(strnew)
                L.append(L1)
                L1=[]
        return L

obj = Solution({'a':['b'], 'b':['d','c'], 'c':['a'],'d':['e'],'e':['f'], 'f':['d'],'g':['f','h'],'h':['i'],'i':['j'],'j':['g','k'],'k':[]})
result = obj.dfs_main({'a':['b'], 'b':['d','c'], 'c':['a'],'d':['e'],'e':['f'], 'f':['d'],'g':['f','h'],'h':['i'],'i':['j'],'j':['g','k'],'k':[]})