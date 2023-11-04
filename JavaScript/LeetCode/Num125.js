/**
 * Date: 23.11.04
 * Number: LeetCode 125
 * Title: Valid Palindrome
 * Level: Easy
 * Author: thelight0804
 */

/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function(s) {
    // convert lowercase
    s = s.toLowerCase();
    var l = 0; // left
    var r = s.length - 1; // right

    // traverse string with left and right
    while (l < r){
        // check alphanumeric character
        if (!isAlnum(s[l])){
            l++;
            // jump to next while, if alphanumeric character is not consecutive
            continue;
        }
        if (!isAlnum(s[r])){
            r--;
            continue;
        }

        // check same character
        if (s[l] !== s[r]) return false

        // move next step
        l++;
        r--;
    }

    return true;
};

/**
 * 
 * @param {character} char
 * @returns {boolean} return true if character is alphanumeric character, otherwise return false
 */
function isAlnum(char){
    return char.match(/^[0-9a-z]+$/) ? true : false;
}