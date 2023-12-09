

class Solution:
    def __init__(self, graph):
       self.graph = graph

    def dfs_graph_reverse(self, graph, visited, stack, node, strnew):
        visited.add(node)
        for j in graph[node]:
            if not j in visited:
                self.dfs_graph_reverse(graph, visited, stack, j, strnew)
                print(stack)
    # if all neighbors have been visited add the node to string.
        # since string is immutable, strnew doesn't change
        strnew += str(node)
        stack.append(node)
        print(stack)
        return


    def dfs_main(self, graph):

        strnew=''
        visited=set()
        stack=[]

        for elem in graph.keys():
            #print(visited)
            if not elem in visited:
               # print(elem)
                self.dfs_graph_reverse(graph, visited, stack, elem, strnew)

        return strnew, stack

obj = Solution({'g':['j'], 'j':['i'], 'i':['h'], 'h':['g']})
result, res = obj.dfs_main({'g':['j'], 'j':['i'], 'i':['h'], 'h':['g']})