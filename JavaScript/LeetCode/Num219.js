/**
 * Date: 23.10.16
 * Number: LeetCode 219
 * Title: Contains Duplicate II
 * Level: Easy
 * Author: thelight0804
 */


/**
 * @param {number[]} nums
 * @param {number} k
 * @return {boolean}
 */
var containsNearbyDuplicate = function(nums, k) {
    // create map object
    var map = new Map();

    for (var i = 0; i < nums.length; i++){
        var n = nums[i];
        // current index - previous index is less than k
        if (i - map.get(n) <= k) return true;
        // set (number, index)
        else map.set(n, i);
    }
    // do not match conditions
    return false
};