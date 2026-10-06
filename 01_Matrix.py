# Time Complexity : O(MN)
# Space Complexity : O(MN)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No

# Your code here along with comments explaining your approach
# Using BFS. Intialize a queue and iterate over the matrix and if we find 1 in the matrix update it to -1 and if we find 0 append it to queue
# Until queue is empty iterate over the queue and pop the indexes i and j
# Initialize a list of tuples with the 4 directions or neighbors
# Iterate over the neighbors and get the row and col index by adding i and j with each neighbor
# Check the boundaries of row and col and check if the matrix[i][j] == -1 then append it to queue
# Update the matrix at index row and col to original matrix at index i and j + level until for each level until the queue is not empty
# Then return matrix


from collections import deque
class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        if not mat:
            return []
        queue = deque()
        level = 1
        dirs = {(0,1), (1,0), (0,-1), (-1,0)}
        m = len(mat)
        n = len(mat[0])
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    queue.append((i,j))
                else:
                    mat[i][j] = -1

        while queue:
            size = len(queue)
            for i in range(size):
                row, col = queue.popleft()
                for dir in dirs:
                    r = row + dir[0]
                    c = col + dir[1]
                    if r >= 0 and r < m and c >= 0 and c < n and mat[r][c] == -1:
                        mat[r][c] = level
                        queue.append((r,c))
            level += 1
        return mat
#BFS

class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        if not mat:
            return []
        self.m = len(mat)
        self.n = len(mat[0])
        for i in range(self.m):
            for j in range(self.n):
                if mat[i][j] == 1:
                    mat[i][j] = float('inf')
        for i in range(self.m):
            for j in range(self.n):
                if mat[i][j] == 0:
                    self.helper(mat, i, j, 0)

        
        return mat

    def helper(self, mat, r, c, dist):
        if r < 0 or r >= self.m or c < 0 or c >= self.n or mat[r][c] < dist:
            return
        mat[r][c] = dist
        dirs = {(0,1), (1,0), (0,-1), (-1,0)}
        for dir in dirs:
            row = r + dir[0]
            col = c + dir[1]
            self.helper(mat, row, col, dist+1)
        
            



        

        