# Time Complexity : O(MN)
# Space Complexity : O(MN)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No

# Your code here along with comments explaining your approach
# Using BFS. Check the base condition if the color at given index = newColor then return image
# If not then assign the startcolor at given index to newcolor
# Initialize a queue and append the indexes sr,sc to the queue
# Until queue is empty iterate over the queue and pop the indexes i and j
# Initialize a list of tuples with the 4 directions or neighbors
# Iterate over the neighbors and get the row and col index by adding i and j with each neighbor
# Check the boundaries of row and col and check if the color at new index row and col is equal to the startcolor at given index then append it to queue
# Update the color at index row and col to newcolor until for each level until the queue is not empty
# Then return image

from collections import deque
class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        startcolor = image[sr][sc]
        if startcolor == color:
            return image
        image[sr][sc] = color
        queue = deque([(sr,sc)])
        m = len(image)
        n = len(image[0])
        dirs = {(0,1), (1,0), (0,-1), (-1,0)}
        while queue:
            row, col = queue.popleft()
            for dir in dirs:
                r = row + dir[0]
                c = col + dir[1]
                if r >= 0 and r < m and c >= 0 and c < n and image[r][c] == startcolor:
                    image[r][c] = color
                    queue.append((r,c))
        return image
#BFS

class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        self.startcolor = image[sr][sc]
        self.m = len(image)
        self.n = len(image[0])
        if image[sr][sc] == color:
            return image
    
        def helper(image, r, c, color):
            if r < 0 or r >= self.m or c < 0 or c >= self.n:
                return
            if image[r][c] != self.startcolor:
                return
            image[r][c] = color
            dirs = {(0,1), (1,0), (0,-1), (-1,0)}
            for dir in dirs:
                row = r + dir[0]
                col = c + dir[1]
                helper(image, row, col, color)

        helper(image, sr, sc, color)
        return image
        