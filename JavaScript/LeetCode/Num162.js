/**
 * Date: 23.08.29
 * Number: LeetCode 162
 * Title: Find Peak Element
 * Level: Medium
 * Author: thelight0804
 */

//O(log n)
/**
 * @param {number[]} nums
 * @return {number}
 */
var findPeakElement = function(nums) {
    let left = 0; //left index
    let right = nums.length - 1; //right index

    if(right === 0) return 0;

    while(left < right){
        let pivot = Math.floor((left + right) / 2); //middle index
        let num = nums[pivot];
        let nextNum = nums[pivot + 1];

        //move left or right
        num < nextNum ? left = pivot + 1 : right = pivot;
    }

    return right; //result
};

//O(n)
var findPeakElement = function(nums) {
    if(nums.length === 1) return 0;

    let i = 0; //array index
    
    while(i < nums.length - 1){
        let num = nums[i]; //value
        let nextNum = nums[i+1]; //next value

        if(num > nextNum) return i; //return peak
        else i++; //move next
    }

    return i; //return last index
};