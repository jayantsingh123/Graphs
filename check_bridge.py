class Solution:

    def __init__(self):
        pass
    def check_bridge(self, graph,V, c, d):
        """ is the edge from c to d a bridge in the graph.
        Idea: Check if there are more than one ways to go from vertex c to vertex d
        Return True if bridge else False"""
        q=[c]
        visited=[False]*V
        visited[c]=True
        while len(q) > 0:
            elem = q.pop(0)
            for j in graph[elem]:
                if not visited[j]:
                    visited[j]=True
                    if j!=d:
                        q.append(j)
                else:
                    if j == d:
                        return False
        return True

if __name__=="__main__":
    obj = Solution()
    res = obj.check_bridge([[1,3],[0,4],[3,4],[0,2,4],[1,2,3]],5, 0,3)
