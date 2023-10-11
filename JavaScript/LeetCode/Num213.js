/**
 * Date: 23.10.12
 * Number: LeetCode 213
 * Title: House Robber II
 * Level: Medium
 * Author: thelight0804
 */

/**
 * @param {number[]} nums
 * @return {number}
 */
var rob = function (nums) {
    if (nums.length < 4) {
        return Math.max(...nums);
    }

    // plan1 is rob houses 0 to end - 1
    var plan1 = new Array(...nums);
    // plan2 is rob houses 1 to end
    var plan2 = new Array(...nums);

    // plan1
    plan1[2] += plan1[0];

    for (var i = 3; i < plan1.length - 1; i++){
        plan1[i] += Math.max(plan1[i - 3], plan1[i - 2]);
    }

    // get maximum money of plan1
    var money1 = Math.max(plan1[plan1.length - 3], plan1[plan1.length - 2]);
    

    // plan2
    plan2[3] += plan2[1];

    for (var i = 4; i < plan2.length; i++){
        plan2[i] += Math.max(plan2[i - 3], plan2[i - 2]);
    }

    // get maximum money of plan1
    var money2 = Math.max(plan2[plan2.length - 2], plan2[plan2.length - 1]);

    console.log(plan1)
    console.log(plan2)

    // return maximum money of plan1 or plan2
    return Math.max(money1, money2);
};