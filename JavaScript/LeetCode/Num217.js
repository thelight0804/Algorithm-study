/**
 * Date: 23.10.16
 * Number: LeetCode 217
 * Title: Contains Duplicate
 * Level: Easy
 * Author: thelight0804
 */


// use Array.sort
/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {
    // sort array
    nums.sort((a, b) => a - b);

    var prev = null; // previous number of nums
    for(var n of nums){
        // appears twice value in the array
        if (prev === n) return true;
        // set previous number
        prev = n;
    }

    // not twice value in the array
    return false;
};

// Use Hash table
var containsDuplicate = function(nums) {
    // Create new hash table(Map object)
    var map = new Map();

    for (var n of nums){
        // appears twice value in the array
        if (map.get(n)) return true;
        // appear first value
        else map.set(n, true);
    }

    // not twice value in the array
    return false;
};

// Use Set object
var containsDuplicate = function(nums) {
    // create set object
    var set = new Set(nums);
    return set.size != nums.length;
};