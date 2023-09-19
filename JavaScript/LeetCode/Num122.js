/**
 * Date: 23.09.19
 * Number: LeetCode 122
 * Title: Best Time to Buy and Sell Stock II
 * Level: Medium
 * Author: thelight0804
 */

/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    var profit = 0;

    for (var i = 0; i < prices.length; i++){
        var prev = prices[i - 1]; // last price
        var current = prices[i]; // current price

        // add profit
        if (prev < current){
            profit += current - prev;
        }
    }

    return profit;
};