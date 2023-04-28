/*
Date:
  23.04.28
Number:
  LeetCode 283
Title:
  Move Zeroes
Level:
  Easy
Author:
  thelight0804
*/

////use two pointer
/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var moveZeroes = function(nums) {  
  for(var i = 0; i < nums.length; i++){
    if(nums[i] === 0){
      for(var j = i + 1; j < nums.length; j++){
        //search not 0 number
        if(nums[j] !== 0){
          //swap 0 to number
          nums[i] = nums[j];
          nums[j] = 0;
          break;
        }
      }
    }
  }
};

////not pointer
/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var moveZeroes = function(nums) {
  var count = 0; //not zero count
  for(var i = 0; i < nums.length; i++){
    if(nums[i] !== 0){ //search not zero
      nums[count] = nums[i]; //set number
      count ++;
    }
  }
  //fill zero
  for(; count < nums.length; count++){
    nums[count] = 0;
  }
};