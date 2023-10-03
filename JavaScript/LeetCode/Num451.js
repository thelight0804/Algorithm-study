/**
 * Date: 23.10.03
 * Number: LeetCode 451
 * Title: Sort Characters By Frequency
 * Level: Medium
 * Author: thelight0804
 */

/**
 * @param {string} s
 * @return {string}
 */
var frequencySort = function(s) {
    var map = new Map();

    // traverse string
    for (var key of s){
        // count + 1 of character
        if (map.get(key)){
            map.set(key, map.get(key) + 1);
        }
        // set new character:count
        else {
            map.set(key, 1);
        }
    }

    // sort map by count
    map = [...map.entries()].sort((a, b) => b[1] - a[1]);
    var result = ""; // new string
    
    // create new string
    for (var [char, count] of map){
        for (var i = 0; i < count; i++){
            result += char;
        }
    }

    return result;
};