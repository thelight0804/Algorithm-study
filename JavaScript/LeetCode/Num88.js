/**
 * Date: 23.08.28
 * Number: LeetCode 88
 * Title: Merge Sorted Array
 * Level: Easy
 * Author: thelight0804
 */

//Use Two pointers
/**
 * @param {number[]} nums1
 * @param {number} m
 * @param {number[]} nums2
 * @param {number} n
 * @return {void} Do not return anything, modify nums1 in-place instead.
 */
var merge = function(nums1, m, nums2, n) {
    //set index
    let idx1 = m - 1; //max nums1 index
    let idx2 = n - 1; //max nums2 index
    let idx3 = nums1.length - 1; //end of nums1
    
    while(idx3 >= 0){
        //end order of nums2
        if(idx2 < 0) return;

        //get num through index
        let num1 = nums1[idx1];
        let num2 = nums2[idx2];

        if(num1 >= num2){
            nums1[idx3] = nums1[idx1];
            idx1--;
            idx3--;
        }
        else if(num1 < num2 || idx1 < 0){
            nums1[idx3] = nums2[idx2];
            idx2--;
            idx3--; 
        }
    }
};

//Use array.sort()
var merge = function(nums1, m, nums2, n) {
    for(let i = m, j = 0; j < n; i++, j++){ //1
        nums1[i] = nums2[j];
    }
    nums1.sort((a, b) => a - b); //2
};