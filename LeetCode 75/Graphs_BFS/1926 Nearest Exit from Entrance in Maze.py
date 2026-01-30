class Solution:

    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
    
        def check_exit(loc):
            row = loc[0]
            col = loc[1]
            if loc != entrance:
                if row == 0 or row == len(maze)-1 or col == 0 or col == len(maze[0])-1:
                    return True
            return False
        
        def add_cells(loc):

            depth = loc[1]
            loc = loc[0]

            res = []

            row = loc[0]
            col = loc[1]

            if row-1 >= 0 and maze[row-1][col] == ".":
                que.append(([row-1, col], depth+1))
                maze[row-1][col] = "+"
            if row+1 < len(maze) and maze[row+1][col] == ".":
                que.append(([row+1, col], depth+1))
                maze[row+1][col] = "+"
            if col-1 >= 0 and maze[row][col-1] == ".":
                que.append(([row, col-1], depth+1))
                maze[row][col-1] = "+"
            if col+1 < len(maze[0]) and maze[row][col+1] == ".":
                que.append(([row, col+1], depth+1))
                maze[row][col+1] = "+"

        depth = 0
        loc = (entrance, 0)
        que = [loc]
        ans = []

        def bfsRec(loc):
            
            if check_exit(loc[0]):
                return loc[1]

            add_cells(loc)
            que.pop(0)                    
            
            if que:
                return bfsRec(que[0])
                
            return -1
        
        return bfsRec(loc)



