/**
 * Date: 23.10.17
 * Number: LeetCode 242
 * Title: Valid Anagram
 * Level: Easy
 * Author: thelight0804
 */


// Use sort
/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function(s, t) {
    // chech two strings length
    if (s.length !== t.length) return false;

    // sort string in ascending order 
    s = s.split('').sort().join('');
    t = t.split('').sort().join('');
    
    // check same string
    return s===t;
};

// Use hash table
var isAnagram = function(s, t) {
    // chech two strings length
    if (s.length !== t.length) return false;

    // Create Hash map(hash table)
    var map = new Map();

    // Traverse s character
    for (var char of s){
        // Add count of character
        var count = map.get(char);
        if (map.get(char)){
            map.set(char, ++count);
        }
        else {
            // key: character, value: count
            map.set(char, 1);
        }
    }
    
    // Traverse t character
    for (var char of t){
        var count = map.get(char);
        // count is undefined or 0, is not Anagram
        if (!count) return false;
        // decrease count
        else map.set(char, --count);
    }

    // s and t is Anagram
    return true;
};
