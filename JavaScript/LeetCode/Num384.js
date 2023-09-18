/**
 * Date: 23.09.18
 * Number: LeetCode 384
 * Title: Shuffle an Array
 * Level: Medium
 * Author: thelight0804
 */

/**
 * @param {number[]} nums
 */
var Solution = function(nums) {
    this.origianl = nums; // original array
    this.random = [...nums]; // shuffle array
};

/**
 * @return {number[]}
 */
Solution.prototype.reset = function() {
    // return original array
    return this.origianl;
};

/**
 * @return {number[]}
 */
Solution.prototype.shuffle = function() {
    var random = this.random;

    // Fisher–Yates shuffle
    for (var i = 0; i < random.length; i++){
        var idx = Math.floor(Math.random() * random.length);
        [random[i], random[idx]] = [random[idx], random[i]];
    }

    return random;
};

/** 
 * Your Solution object will be instantiated and called as such:
 * var obj = new Solution(nums)
 * var param_1 = obj.reset()
 * var param_2 = obj.shuffle()
 */