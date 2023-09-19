/**
 * Date: 23.09.19
 * Number: LeetCode 121
 * Title: Best Time to Buy and Sell Stock
 * Level: Easy
 * Author: thelight0804
 */

/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    if (prices.length === 1) return 0;

    var p1 = 0; // min pointer
    var p2 = 1; // max pointer
    var profit = 0;

    while (p2 < prices.length){
        var left = prices[p1];
        var right = prices[p2];

        // get current price
        if (left < right){
            var price = right - left;
            // get maximum profit
            profit = Math.max(profit, price);
        }
        else {
            p1 = p2; // set min pointer
        }
        p2++; // move next
    }

    return profit;
};