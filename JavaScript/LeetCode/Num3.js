/**
 * Date: 23.09.10
 * Number: LeetCode 3
 * Title: Longest Substring Without Repeating Characters
 * Level: Medium
 * Author: thelight0804
 */

/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
    if (s.length < 2) return s.length;

    var maxLength = 0; // 
    var map = new Map();
    var l = 0; // left

    for (let r = 0; r < s.length; r++){
        if (map.get(s[r])){
            // move left
            l = Math.max(map.get(s[r]), l);
        }
        // set max length
        maxLength = Math.max(maxLength, r - l + 1);
        // set character, next right index
        map.set(s[r], r + 1);
    }

    return maxLength;
};