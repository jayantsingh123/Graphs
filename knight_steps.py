class Solution:

    def __init__(self):
        pass

    def is_valid(self, row, col, nrows, ncols):
        return 0 <= row <= nrows - 1 and 0 <= col <= ncols - 1

    def minStepToReachTarget(self, KnightPos, TargetPos, N):
        """ find minimum number of steps a Knight
        can take in a square chessboard to get from source to target.
        Note that a knight can take one of following actions;
         a.) two steps horizontal followed by one step vertical,
          b.) tow vertical steps followed by one horizontal step."""

        if KnightPos==TargetPos:
            return 0
        from collections import defaultdict
        nrows, ncols = N, N
        q = []
        dnew = defaultdict(int)
        q.append((KnightPos[0] - 1, KnightPos[1] - 1))
        visited = [[False] * ncols for _ in range(nrows)]
        visited[KnightPos[0] - 1][KnightPos[1] - 1] = True
        dx = [2, 2,-2,-2, 1, -1, 1, -1]
        dy = [1, -1,1, -1,2, 2, -2, -2]
        while len(q) > 0:
            elem = q.pop(0)
            for i in range(len(dx)):
                newrow = elem[0] + dy[i]

                newcol = elem[1] + dx[i]
                if self.is_valid(newrow, newcol, nrows, ncols):
                    if not visited[newrow][newcol]:
                        visited[newrow][newcol] = True
                        q.append((newrow, newcol))
                        dnew[(newrow, newcol)] = dnew[elem] + 1
                        #print(dnew[(newrow,newcol)],(newrow,newcol),elem)
                        if newrow == TargetPos[0] - 1 and newcol == TargetPos[1] - 1:
                            return dnew[(newrow, newcol)]
        return -1
if __name__=="__main__":
    obj = Solution()
    res = obj.minStepToReachTarget((6,1),(2,4),7)

