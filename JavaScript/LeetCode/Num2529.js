/**
 * Date: 23.09.03
 * Number: LeetCode 2529
 * Title: Maximum Count of Positive Integer and Negative Integer
 * Level: Easy
 * Author: thelight0804
 */

/**
 * @param {number[]} nums
 * @return {number}
 */
var maximumCount = function(nums) {
    if (nums[0] > 0 || nums[nums.length - 1] < 0){
        return nums.length;
    }

    var l = 0; // left
    var r = nums.length - 1; // right
    var pos = 0; // positive integer
    var neg = 0; // negative integer

    // find negative integer use binary search
    while (l <= r){
        let pivot = Math.floor((l + r) / 2);
        let num = nums[pivot];

        // move pivot
        if (num < 0) l = pivot + 1;
        else if (num >= 0) r = pivot - 1;
    }

    // counting negative integer
    neg = l; 

    // find positive integer use binary search
    r = nums.length - 1;
    while (l <= r){
        let pivot = Math.floor((l + r) / 2);
        let num = nums[pivot];

        if (num > 0) r = pivot - 1;
        else if (num <= 0) l = pivot + 1;
    }

    // counting negative integer
    pos = nums.length - l 

    return Math.max(neg, pos);
};