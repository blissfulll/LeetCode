class Solution:

    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        
        def check_exit(loc):
            row = loc[0]
            col = loc[1]
            if loc != entrance:
                if row == 0 or row == len(maze)-1 or \
                    col == 0 or col == len(maze[0])-1:
                    return True
            return False
        
        def check_cell(loc):

            depth = loc[1]
            loc = loc[0]

            if check_exit(loc):
                return True

            res = [()]

            row = loc[0]
            col = loc[1]

            if row-1 >= 0 and maze[row-1][col] != "+":
                res.append(([row-1, col], depth))
            if row+1 < len(maze) and maze[row+1][col] != "+":
                res.append(([row+1, col], depth))
            if col-1 >= 0 and maze[row][col-1] != "+":
                res.append(([row, col-1], depth))
            if col+1 < len(maze[0]) and maze[row][col+1] != "+":
                res.append(([row, col+1], depth))

            return res

        depth = 0
        loc = (entrance, 0)
        que = [loc]
        visited = []
        ans = []

        def bfsRec(loc):
            # print(loc)
            visited.append(loc[0])
            que.pop(0)
            # depth+=1
            res = check_cell(loc)
            # print(res, depth)
            if res == True:
                # print("HHAHAHSHAHA")
                ans.append(loc[1])
            else:
                if res == [()]:
                    pass
                else:
                    for loc in res:
                        print(loc)
                        if loc[0] not in visited:
                            que.append((loc[0], loc[1]+1))

                if que:
                    bfsRec(que[0])
        
        bfsRec(loc)

        if ans:
            return ans[0]

        return -1



