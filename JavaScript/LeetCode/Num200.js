/**
 * Date: 23.07.05
 * Number: LeetCode 200
 * Title: Number of Islands
 * Level: Medium
 * Author: thelight0804
 */

/**
 * @param {character[][]} grid
 * @return {number}
 */
var numIslands = function(grid) {
    var count = 0; //Island count
    var rows = grid.length;
    var cols = grid[0].length;

    function dfs(y, x){
        //check land or water
        if(grid[y][x] === "1"){
            grid[y][x] = "0"; //searched land
        }
        else{
            return;
        }


        if(x < cols - 1){ //move right
            dfs(y, x+1);
        }
        //move right
        if(y < rows - 1){ //move down
            dfs(y+1, x);
        }
        if(x > 0){ //move left
            dfs(y, x-1);
        }
        if(y > 0){ //move up
            dfs(y-1, x);
        }
    }

    //search 1 in grid
    for(var row = 0; row < rows; row++){
        for(var col = 0; col < cols; col++){
            if(grid[row][col] === "1"){
                //found first land
                dfs(row, col)
                count ++;
            }
        }
    }

    return count;
};