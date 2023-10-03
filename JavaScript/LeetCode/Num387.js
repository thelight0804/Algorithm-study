/**
 * Date: 23.10.03
 * Number: LeetCode 387
 * Title: First Unique Character in a String
 * Level: Easy
 * Author: thelight0804
 */

// hashmap = key: count
/**
 * @param {string} s
 * @return {number}
 */
var firstUniqChar = function(s) {
    var map = new Map();

    // traverse string
    for (var char of s){
        // again to find character
        if (map.get(char)){
            map.set(char, map.get(char) + 1);
        }
        // set count of new character
        else {
            map.set(char, 1);
        }
    }

    // find one count in map
    for (var i = 0; i < s.length; i++){
        if (map.get(s[i]) === 1)
            return i;
    }

    // no non-repeating character
    return -1;
};


// hashmap = key: [index]
/**
 * @param {string} s
 * @return {number}
 */
var firstUniqChar = function(s) {
    var map = new Map();

    // traverse string
    for (var i = 0; i < s.length; i++){
        // again to find character
        if (map.get(s[i])){
            // add index in value array
            var temp = map.get(s[i]);
            temp.push(i);
            map.set(s[i], temp);
        }
        // set new key
        else {
            map.set(s[i], [i]);
        }
    }
    
    // find one index in map
    for (var [key, val] of map){
        if (val.length === 1){
            return val[0];
        }
    }

    // no non-repeating character
    return -1;
};