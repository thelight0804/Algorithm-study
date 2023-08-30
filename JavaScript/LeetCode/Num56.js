/**
 * Date: 23.08.30
 * Number: LeetCode 56
 * Title: Merge Intervals
 * Level: Medium
 * Author: thelight0804
 */

/**
 * @param {number[][]} intervals
 * @return {number[][]}
 */
 
var merge = function(intervals) {
    if(intervals.length === 1) return intervals; 

    intervals.sort((a,b) => a[0] - b[0]); //sort of array first value

    let result = [];
    let temp = intervals[0]; //temp array

    for(let i = 0; i < intervals.length; i++){
        if(intervals[i][0] <= temp[1]){ //set max
            temp[1] = Math.max(intervals[i][1], temp[1]);
        }
        else{ //append array to result
            result.push(temp);
            temp = intervals[i]; //new temp array
        }
    }

    result.push(temp); //append last temp array to result

    return result;
};