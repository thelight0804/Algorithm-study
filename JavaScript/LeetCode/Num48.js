/**
 * Date: 23.09.01
 * Number: LeetCode 48
 * Title: Rotate Image
 * Level: Easy
 * Author: thelight0804
 */

/**
 * @param {number[][]} matrix
 * @return {void} Do not return anything, modify matrix in-place instead.
 */
var rotate = function(matrix) {
    let len = matrix.length;

    //matrix[i][j] reverse to matrix[j][i]
    for(let i = 0; i < len; i++){
        for(let j = i; j < len; j++){
            let temp = matrix[j][i];
            matrix[j][i] = matrix[i][j];
            matrix[i][j] = temp;
        }
    }

    //reverse of 1D array
    for(let i = 0; i < len; i++){
        for(let j = 0; j < len/2; j++){
            let x = -j + len - 1;

            let temp = matrix[i][x];
            matrix[i][x] = matrix[i][j];
            matrix[i][j] = temp;
        }
    }
};