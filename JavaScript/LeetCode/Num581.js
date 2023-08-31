/**
 * Date: 23.08.31
 * Number: LeetCode 581
 * Title: Shortest Unsorted Continuous Subarray
 * Level: Medium
 * Author: thelight0804
 */

//O(n)
/**
 * @param {number[]} nums
 * @return {number}
 */
var findUnsortedSubarray = function(nums) {
    if(nums.length < 2) return 0;

    let max = nums[0];
    let min = nums[nums.length - 1];
    let left = -1;
    let right = -1;

    for(let i = 1; i < nums.length; i++){
        let a = nums[i]; //left to right
        let b = nums[nums.length - i - 1]; //right to left
        a < max ? right = i : max = a; //find max
        b > min ? left = i : min = b; //find min
    }

    return Math.max(0, left + right - nums.length + 2);
};

//O(n*log n)
var findUnsortedSubarray = function(nums) {
    if(nums.length < 2) return 0;

    //sort nums to new array
    let sortArr = [...nums].sort((a, b) => a - b);
    let i = 0;
    let j = 0;

    //find another value form nums and sortArr
    //left
    for(i = 0; i < nums.length; i++){
        let a = nums[i];
        let b = sortArr[i];

        if(a != b) break;
        //all values are same
        else if(i === nums.length - 1) return 0;
    }

    //right
    for(j = nums.length - 1; j > 0; j--){
        let a = nums[j];
        let b = sortArr[j];

        if(a != b){
            j++;
            break;
        }
    }

    //return count
    return Math.abs(j - i);
};