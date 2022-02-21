from code_200_number_of_islands import Solution

def test_example_1():
    s = Solution()
    grid = [
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
    ]
    output = 1
    assert s.numIslands(grid) == output