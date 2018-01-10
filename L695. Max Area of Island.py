# Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

# Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)

# Example 1:
# [[0,0,1,0,0,0,0,1,0,0,0,0,0],
#  [0,0,0,0,0,0,0,1,1,1,0,0,0],
#  [0,1,1,0,1,0,0,0,0,0,0,0,0],
#  [0,1,0,0,1,1,0,0,1,0,1,0,0],
#  [0,1,0,0,1,1,0,0,1,1,1,0,0],
#  [0,0,0,0,0,0,0,0,0,0,1,0,0],
#  [0,0,0,0,0,0,0,1,1,1,0,0,0],
#  [0,0,0,0,0,0,0,1,1,0,0,0,0]]
# Given the above grid, return 6. Note the answer is not 11, because the island must be connected 4-directionally.
# Example 2:
# [[0,0,0,0,0,0,0,0]]
# Given the above grid, return 0.
# Note: The length of each dimension in the given grid does not exceed 50.

class Solution:

    right_bound = None
    bottom_bound = None

    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        self.right_bound = len(grid[0])-1
        self.bottom_bound = len(grid)-1
        
        x = 0
        y = 0
        max_area = 0
        while x < len(grid):
            y = 0
            while y < len(grid[x]):
                if self.get_element(x, y, grid) == 1:
                    temp = self.max_area_dfs(x, y, grid)
                    if max_area < temp:
                        max_area = temp
                y += 1
            x += 1

        return max_area

    def max_area_dfs(self, x, y, grid):
                
        if not self.get_element(x,y, grid):
            return 0
        
        count = 1
        grid[x][y] = 0
        
        return count + self.max_area_dfs(x,y-1, grid) + self.max_area_dfs(x, y+1, grid) + self.max_area_dfs(x-1, y, grid) + self.max_area_dfs(x+1, y, grid)



    def get_element(self, x, y, grid):
        if x >= 0 and x <= self.bottom_bound:
            if y>=0 and y <= self.right_bound:
                return grid[x][y]
        return 0

grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]

# grid = [[0,1,1],[0,1,0]]


print(Solution().maxAreaOfIsland(grid))