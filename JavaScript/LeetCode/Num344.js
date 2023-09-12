/**
 * Date: 23.09.12
 * Number: LeetCode 344
 * Title: Reverse String
 * Level: Easy
 * Author: thelight0804
 */

/**
 * @param {character[]} s
 * @return {void} Do not return anything, modify s in-place instead.
 */
var reverseString = function(s) {
    var l = 0; //left index
    var r = s.length - 1; //right index

    while (l < r){
        // swap reverse
        [s[l], s[r]] = [s[r], s[l]];

        // move index
        l++;
        r--;
    }
};