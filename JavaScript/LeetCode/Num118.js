/**
 * Date: 23.11.06
 * Number: LeetCode 118
 * Title: Pascal's Triangle
 * Level: Easy
 * Author: thelight0804
 */


/**
 * @param {number} numRows
 * @return {number[][]}
 */
var generate = function(numRows) {
    // initialize pascal's array
    var pascal = [];

    // generate new pascal values
    for (var i = 0; i < numRows; i++){
        pascal[i] = [];
        pascal[i][0] = 1; // set first number

        // get new number from previous pascal value
        for (var j = 1; j < i; j++){
            pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j];
        }
        // set last number
        pascal[i][i] = 1;
    }

    return pascal;
};