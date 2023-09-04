/**
 * Date: 23.09.04
 * Number: LeetCode 240
 * Title: Search a 2D Matrix II
 * Level: Medium
 * Author: thelight0804
 */

// O(m+n)
/**
 * @param {number[][]} matrix
 * @param {number} target
 * @return {boolean}
 */
var searchMatrix = function(matrix, target) {
    //search 2D array
    while(matrix.length > 0){
        var len = matrix[0].length;
        var num = matrix[0][len - 1];
        
        if (target === num) return true;
        else if (target < num){
            for(var j = 0; j < matrix.length; j++){
                matrix[j].splice(len - 1);
            }
        }
        else{
            matrix.splice(0, 1);
        }
    }
    return false;
};

// O(n log(m))
var searchMatrix = function(matrix, target) {
    //search 2D array
    for(let i = 0; i < matrix.length; i++){
        var arr = matrix[i]; //get 1D array from 2D array
        var l = 0; //left
        var r = matrix[0].length - 1; //right

        //find target use binary search
        while (l <= r){
            var pivot = Math.floor((l + r) / 2);
            var num = arr[pivot];
            if (num === target) return true;
            else if (target < num) r = pivot - 1;
            else l = pivot + 1;
        }
    }
    return false;
};