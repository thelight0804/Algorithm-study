/**
 * Date: 23.11.02
 * Number: LeetCode 136
 * Title: Single Number
 * Level: Easy
 * Author: thelight0804
 */

/**
 * @param {number[]} nums
 * @return {number}
 */
var singleNumber = function(nums) {
    // initialize single number
    var num = 0;

    for (n of nums){
        // use XOR
        num ^= n;
    }

    return num;
};