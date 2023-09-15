/**
 * Date: 23.09.15
 * Number: LeetCode 70
 * Title: Climbing Stairs
 * Level: Easy
 * Author: thelight0804
 */

/**
 * @param {number} n
 * @return {number}
 */
var climbStairs = function(n) {
    var a = 1; // first step
    var b = 1; // second step

    for (var i = 1; i < n; i++){
        var tmp = a;
        a += b; // add second step to a
        b = tmp;
    }
    
    return a;
};