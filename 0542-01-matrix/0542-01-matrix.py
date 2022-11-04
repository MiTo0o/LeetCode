from collections import deque
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        # faster bfs starting with processing all the 0s 
        # update distance of each adjacent cell to self + 1
        
        visited = set()
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        
        q = deque()
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if mat[i][j] == 0:
                    visited.add((i,j))
                    q.append((i,j))
        
        while q:
            # for i in mat:
            #     print(i)
            # print()
            # print()
            x,y = q.popleft()
            for dir in dirs:
                newX, newY = x + dir[0], y + dir[1]
                if newX >= 0 and newX <= len(mat) - 1 and newY >= 0 and newY <= len(mat[0]) - 1 and (newX, newY) not in visited:
                        mat[newX][newY] = mat[x][y] + 1
                        visited.add((newX, newY))
                        q.append((newX, newY))
        return mat   
        
        
        
# slow naive bfs      
    
#         def helper(m, i, j):
#             q = deque()
#             q.append(((i, j), 0))
#             seen = ()
#             dirs = [(1,0), (-1,0), (0,1), (0,-1)]
#             while q:
#                 coord, d = q.popleft()
#                 x, y = coord
#                 if m[x][y] == 0:
#                     return d
#                 for dir in dirs:
#                     newX, newY = x + dir[0], y + dir[1]
#                     if newX >= 0 and newX <= len(m) - 1 and newY >= 0 and newY <= len(m[0]) - 1:
#                         if (newX, newY) not in seen:
#                             q.append(((newX, newY), d+1))
#             return -1
        
#         xd = []
#         for i in range(len(mat)):
#             for j in range(len(mat[0])):
#                 if mat[i][j] == 0:
#                     xd.append(0)
#                 else:
#                     xd.append(helper(mat, i, j))
#         return [xd[i*len(mat[0]):(i+1)*len(mat[0])] for i in range(len(mat))]
        