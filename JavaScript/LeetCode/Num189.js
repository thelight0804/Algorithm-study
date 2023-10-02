/**
 * Date: 23.10.02
 * Number: LeetCode 189
 * Title: Rotate Array
 * Level: Medium
 * Author: thelight0804
 */

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var rotate = function(nums, k) {
    var len = nums.length;

    // get k step in nums
    k %= len;


    swap(nums, 0, len - 1) // reverse all elements in nums
    swap(nums, 0, k-1) // reverse front elements in nums
    swap(nums, k, len - 1) // reverse last elements in nums

    // reverse funtion
    function swap(nums, start, end){
        for (; start < end; start++, end--){
            var temp = nums[end];
            nums[end] = nums[start];
            nums[start] = temp;
        }
        
        return nums;
    }

    return nums;
};