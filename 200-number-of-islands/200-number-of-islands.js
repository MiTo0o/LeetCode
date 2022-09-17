/**
 * @param {character[][]} grid
 * @return {number}
 */
var numIslands = function(grid) {
    let numOfIslands = 0
    for (let i = 0; i < grid.length; i++) {
        for (let j = 0; j < grid[0].length; j++) {
            if (grid[i][j] === '1') {
                numOfIslands++;
                markIsland(grid, i, j);
            }
        }
    }
    return numOfIslands;
};

const markIsland = function(grid, i, j) {
    if (grid[i][j] !== '1') {
        return
    }
    grid[i][j] = '0';
    if (i + 1 < grid.length) {
        markIsland(grid, i + 1, j)
    }
    if (i - 1 >= 0) {
        markIsland(grid, i - 1, j)
    }
    if (j + 1 < grid[0].length) {
        markIsland(grid, i, j + 1)
    }
    if (j - 1 >= 0) {
        markIsland(grid, i, j - 1)
    }
}