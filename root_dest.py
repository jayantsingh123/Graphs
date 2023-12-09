class Solution:

    def __init__(self, graph):
        self.graph = graph

    def helper(self, graph, node, res, listnew):
        res.append(node)
        print(res, listnew)
        if node == len(graph) - 1:
           # print(res,listnew)
            listnew.append(res)
            print(listnew)
        else:
            for nodenew in graph[node]:
                self.helper(graph, nodenew, res, listnew)
        res.pop()
        print(res,listnew)
        return

    def source_to_target_paths(self, graph):
        res, listnew = [], []
        node = 0
        self.helper(graph, node, res, listnew)
        return listnew
obj = Solution([[1,2],[4],[3,4],[4],[0]])
result = obj.source_to_target_paths([[1,2],[4],[3,4],[4],[0]])