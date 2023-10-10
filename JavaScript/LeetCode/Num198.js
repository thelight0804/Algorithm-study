/**
 * Date: 23.10.10
 * Number: LeetCode 198
 * Title: House Robber
 * Level: Medium
 * Author: thelight0804
 */

/**
 * @param {number[]} nums
 * @return {number}
 */
var rob = function(nums) {
    // when length of nums is 3
    if (nums.length < 3){
        return Math.max(...nums);
    }
    else if (nums.length === 3){
        return Math.max(nums[2] + nums[0], nums[1]);
    }

    // fixed value
    nums[2] += nums[0];

    // dynamic programming
    for (var i = 3; i < nums.length; i++){
        // set max of nums[i-2], nums[i-3]
        nums[i] += Math.max(nums[i - 2], nums[i - 3]);
    }

    // return maximum amount of money
    return Math.max(nums[nums.length - 2], nums[nums.length - 1]);
};