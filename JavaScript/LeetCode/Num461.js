/**
 * Date: 23.10.11
 * Number: LeetCode 461
 * Title: Hamming Distance
 * Level: Easy
 * Author: thelight0804
 */

// Use Bitwise AND (&)
/**
 * @param {number} x
 * @param {number} y
 * @return {number}
 */
var hammingDistance = function(x, y) {
    // Hamming distance count
    var count = 0;

    // get hamming distance count
    for (var i = x ^ y; i > 0; i = i >> 1){
        // XOR is 1, add count 
        if (i & 1) count++;
    }
    
    return count;
};

//Convert binary use toString(2)
var hammingDistance = function(x, y) {
    // convert x XOR y number to binary
    var xor = (x ^ y).toString(2);
    // Hamming distance count
    var count = 0;

    // counting hamming distance
    for (var b of xor){
        if (b === '1') count++;
    }
    
    return count;
};