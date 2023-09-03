/**
 * Date: 23.09.03
 * Number: LeetCode 74
 * Title: Search a 2D Matrix
 * Level: Medium
 * Author: thelight0804
 */

/**
 * @param {number[][]} matrix
 * @param {number} target
 * @return {boolean}
 */
var searchMatrix = function(matrix, target) {
    let pivot = 0;
    let l = 0; // left
    let r = matrix.length - 1; // right

    // 2D array binary search
    while (l <= r){
        pivot = Math.floor((l + r) / 2);
        let a = matrix[pivot][0];
        let b = matrix[pivot][matrix[pivot].length - 1];

        if(target === a || target === b){
            return true
        }
        else if(target > a && target < b){ // go to 1D array
            l = 0;
            r = matrix[pivot].length - 1;
            break;
        }
        else if(target < a){ // set right
            r = pivot - 1;
        }
        else{ // set left
            l = pivot + 1;
        }
    }
    
    // 1D array binary search
    let nums = matrix[pivot];
    
    while (l <= r) {
        pivot = Math.floor((l + r) / 2);
        let num = nums[pivot];

        if (num === target) return true;
        if (num < target) l = pivot + 1;
        else r = pivot - 1;
    }

    return false;
}