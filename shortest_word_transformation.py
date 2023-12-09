class Solution:
    def __init__(self, wordlist):
       self.wordlist = wordlist

    def distance(self, word1, word2):
        L1 = list(word1)
        L2 = list(word2)
        cnt = 0
        if len(word1) == len(word2):
            for k in range(len(L1)):
                if L1[k] != L2[k]:
                    cnt += 1
        if cnt == 1:
            return word2


    def construct_grid(self, word_list, source):
        from collections import defaultdict
        dnew = defaultdict(list)
        if source not in word_list:
            dnew[source] = [self.distance(source, strnew) for j, strnew in enumerate(word_list) if self.distance(source, strnew) is not None]
        for k,v in enumerate(word_list):
            elem = v
            dnew[elem] = [self.distance(elem, strnew) for j, strnew in enumerate(word_list) if j!=k and self.distance(elem, strnew) is not None ]
        return dnew

    def shortest_word_transformation(self, source, target, word_list):
        grid = self.construct_grid(word_list, source)
        if target not in word_list or len(source) != len(target) or len(grid[source])==0:
            return 0
        visited = [False] * len(word_list)
        if source in word_list:
            visited[word_list.index(source)] = True
        q = []
        q.append((source, 1))

        #print(grid)
        while len(q) > 0:
            (elem, cnt) = q.pop(0)
            if elem == target:
                return cnt
            for j in grid[elem]:
               # print(elem, j)
                idx = word_list.index(j)
                if visited[idx] == False:
                    visited[idx] = True
                    q.append((j, cnt + 1))
        return 0

obj = Solution(['tan', 'rose', 'tax'])
result = obj.shortest_word_transformation('red', 'tax', ['tan','rose', 'tax'])



