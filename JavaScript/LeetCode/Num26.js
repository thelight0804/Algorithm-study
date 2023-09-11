/**
 * Date: 23.09.11
 * Number: LeetCode 26
 * Title: Remove Duplicates from Sorted Array
 * Level: Easy
 * Author: thelight0804
 */

/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function(nums) {
    var l = 0; // left index

    for (var r = 1; r < nums.length; r++){
        // save number at left index
        if (nums[l] !== nums[r]){
            l++;
            nums[l] = nums[r];
        }
    }

    // return unique element count
    return l + 1;
};