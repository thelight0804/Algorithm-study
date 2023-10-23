/**
 * Date: 23.10.23
 * Number: LeetCode 190
 * Title: Reverse Bits
 * Level: Easy
 * Author: thelight0804
 */

// calculate binary bit
/**
 * @param {number} n - a positive integer
 * @return {number} - a positive integer
 */
var reverseBits = function(n) {
    var num = 0; // result number
    
    for (var i = 0; i < 32; i++){
        // binary bit is multiply by 2
        num *= 2;
        // add 1 bit
        if (n & 1) num++;
        // move Right shift
        n >>= 1;
    }

    return num;
};


// use array method
var reverseBits = function(n) {
    // convert number to binary bit string.
    var bit = n.toString(2);
    // split bit to array
    // reverse array
    // pad '0' at end.
    var reverseBit = bit.split('').reverse().join('').padEnd(32, '0');
    // convert bit string to int
    return parseInt(reverseBit, 2);
};