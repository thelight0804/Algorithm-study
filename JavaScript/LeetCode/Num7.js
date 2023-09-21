/**
 * Date: 23.09.21
 * Number: LeetCode 7
 * Title: Reverse Integer
 * Level: Medium
 * Author: thelight0804
 */

// reverse number
/**
 * @param {number} x
 * @return {number}
 */
var reverse = function(x) {
    // convert absolute number
    var nums = Math.abs(x);
    var result = 0;

    // reverse integer
    while (nums > 0){
        var num = nums % 10;
        result *= 10;
        result += num;
        nums = Math.floor(nums/10);

        // check 32-bit integer
        if (result > 2 ** 31) return 0;
    }

    // return result
    return x > 0 ? result : result * -1;
};


// convert array string before reverse
var reverse = function(x) {
    // number to string array
    var arr = String(Math.abs(x)).split("");

    // reverse array
    arr.reverse();

    var result = "";
    for (val of arr){
        result += val;
    }

    // check 32-bit integer
    if (result > 2 ** 31){
        return 0;
    }
    else if (x > 0){
        return result;
    }
    else {
        // negative number
        return result * -1;
    }
};