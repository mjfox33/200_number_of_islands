import numpy
class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        OFFSETS = [ (-1,0), (1,0), (0,-1), (0,1) ]
        n = len(grid)
        m = len(grid[0])
        # going to surround the grid by zeros so we dont have to test for row == 0 or n etc
        dp = numpy.pad(grid, 1, mode='constant')

        islands_found = 0
        queue = list()
        for row in range(n):
            for col in range(m):
                if dp[row+1][col+1] == '0':
                    continue
                islands_found += 1
                queue.append((row+1,col+1))
                dp[row+1][col+1] = '0'
                while len(queue) > 0:
                    current_row, current_col = queue.pop()
                    # need to do four tests here
                    for offset in OFFSETS:
                        x = current_row + offset[0]
                        y = current_col + offset[1]

                        if dp[x][y] == '1':
                            dp[x][y] = 0
                            queue.append((x,y))
        return islands_found