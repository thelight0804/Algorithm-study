/**
 * Date: 23.08.31
 * Number: LeetCode 287
 * Title: Find the Duplicate Number
 * Level: Medium
 * Author: thelight0804
 */

//Use array index
/**
 * @param {number[]} nums
 * @return {number}
 */
var findDuplicate = function(nums) {
    for(let i = 0; i < nums.length; i++){ //배열 순회
        let a = Math.abs(nums[i]);
        
        if(nums[a] > 0) nums[a] *= -1; //인덱스의 값을 음수로 변경
        else return a; //이미 음수이면 해당 값 반환
    }
};


//use boolean check of new array
var findDuplicate = function(nums) {
    let arr = new Array(nums.length).fill(false); //배열 생성
    
    for(let i = 0; i < nums.length; i++){
        let a = nums[i]
        if(!arr[a]) arr[a] = true; //true 변경
        else return a; //중복값 반환
    }
};


//sort + brute force
var findDuplicate = function(nums) {
    let sortArr = [...nums].sort((a, b) => a - b); //배열 sort

    for(let i = 0; i < nums.length - 1; i++){ //배열 순회
        let a = sortArr[i];
        let b = sortArr[i + 1];

        if(a === b) return a; //중복값 반환
    }
};