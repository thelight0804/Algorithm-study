/*
Date:
  23.04.28
Number:
  LeetCode 704
Title:
  Binary Search
Level:
  Easy
Author:
  thelight0804
*/

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var search = function(nums, target) {
  //set left, right index
  var left = 0, right = nums.length - 1;

  //until right is big left
  while(left <= right){
    //set pivot index
    var pivot = Math.ceil((left + right) / 2);
    if(nums[pivot] === target) return pivot; //return output
    else if(nums[pivot] < target){
      left = pivot + 1;
    }
    else{// nums[pivot] > target
      right = pivot - 1;
    }
  }
      
  return -1; //target is not exists
};