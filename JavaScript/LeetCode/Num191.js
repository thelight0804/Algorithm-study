/**
 * Date: 23.09.18
 * Number: LeetCode 191
 * Title: Number of 1 Bits
 * Level: Easy
 * Author: thelight0804
 */

// Bit Manipulation
/**
 * @param {number} n - a positive integer
 * @return {number}
 */
var hammingWeight = function(n) {
    var cnt = 0; // bit count

    while (n !== 0) {
        var bit = n & 1; // Bitwise AND (&)
        if (bit === 1) cnt++; // add count
        n >>>= 1; // Unsigned right shift assignment (>>>=)
    }
    return cnt;
};

// sum 1 in array
var hammingWeight = function(n) {
    // convert binary number to array of numbers
    var arr = n.toString(2).split('').map(Number);

    // sum array values
    return arr.reduce((a, b) => a + b, 0);
};