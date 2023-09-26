/**
 * Date: 23.09.26
 * Number: LeetCode 34
 * Title: Find First and Last Position of Element in Sorted Array
 * Level: Medium
 * Author: thelight0804
 */

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var searchRange = function(nums, target) {
    // empty nums
    if (nums.length < 1) return [-1,-1];

    var l = 0; // left index
    var r = nums.length - 1; // right index
    var position = []; // [start, end] index

    // search for start index of target
    while (l < r){
        var pivot = Math.floor((l + r) / 2);

        if (nums[pivot] >= target) r = pivot;
        else l = pivot + 1;
    }

    // not exist target in the array
    if (nums[r] !== target) return [-1,-1]
    // exist target in the array
    else position.push(r);

    // set left and right index
    l = r;
    r = nums.length - 1;

    // search for end index of target
    while (l < r){
        var pivot = Math.floor((l + r) / 2);

        if (nums[pivot] <= target) l = pivot + 1;
        else r = pivot;
    }

    // left was +1, if dismatch target, left -1
    if (nums[l] !== target) l--;

    // push end index
    position.push(l)

    return position;
};