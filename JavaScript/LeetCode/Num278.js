/**
 * Date: 23.09.25
 * Number: LeetCode 278
 * Title: First Bad Version
 * Level: Easy
 * Author: thelight0804
 */

/**
 * Definition for isBadVersion()
 * 
 * @param {integer} version number
 * @return {boolean} whether the version is bad
 * isBadVersion = function(version) {
 *     ...
 * };
 */

/**
 * @param {function} isBadVersion()
 * @return {function}
 */
var solution = function(isBadVersion) {
    /**
     * @param {integer} n Total versions
     * @return {integer} The first bad version
     */
    return function(n) {
        var l = 1; //left index
        var r = n; //right index
        
        while (l < r){
            // get middle pivot
            var pivot = Math.floor((l + r) / 2);

            // binary search
            if (isBadVersion(pivot)){
                r = pivot;
            }
            else{
                l = pivot + 1;
            }
        }
        // return first bad version
        return r;
    };
};