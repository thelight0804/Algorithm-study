/**
 * Date: 23.10.15
 * Number: LeetCode 477
 * Title: Total Hamming Distance
 * Level: Medium
 * Author: thelight0804
 */

/**
 * @param {number[]} nums
 * @return {number}
 */
var totalHammingDistance = function(nums) {
    let total = 0; // total hamming distance

    // loop 0 ~ 32 bit binary
    for(let bit = 0; bit < 32; bit++){
        let count = 0; // get 1 at current bit

        // iterate nums
        for(let j = 0; j < nums.length; j++){
            // add 1 count of nums[j] >> bit
            count += (nums[j] >> bit) & 1;
        }
        // calculate total hamming distance
        total += count * (nums.length - count)
    }

    return total;
};