/**
 * Date: 23.09.04
 * Number: LeetCode 796
 * Title: Rotate String
 * Level: Easy
 * Author: thelight0804
 */

/**
 * @param {string} s
 * @param {string} goal
 * @return {boolean}
 */
var rotateString = function(s, goal) {
    if (s.length !== goal.length) return false;

    s = s.concat(s) //add same string
    return s.includes(goal);
};