/*
Date:
  2023.10.19
Title:
  merge sort
Author:
  thelight0804
*/

var array = [7, 3, 1, 5, 6, 4, 2];
console.log(mergeSort(array))

function mergeSort(arr){
    // 재귀 함수 종료 조건
    // 쪼개져서 하나가 되었다면 반환하기
    if (arr.length === 1){
        return arr;
    }

    // 배열을 절반으로 나누기
    var mid = Math.floor(arr.length / 2);
    var left = arr.slice(0, mid);
    var right = arr.slice(mid);

    //나눈 배열을 다시 쪼개기
    console.log(left, right);
    left = mergeSort(left);
    right = mergeSort(right);

    // 합치기
    var sortedArr = [];
    // 두 배열 모두 존재할 때까지 반복
    while (left.length && right.length){
        // 왼쪽 요소 추가
        if (left[0] <= right[0]){
            sortedArr.push(left.shift());
        }
        else { // 오른쪽 요소 추가
            sortedArr.push(right.shift());
        }
    }

    // 왼쪽 또는 오른쪽에 비어있는 요소 붙이기
    return [...sortedArr, ...left, ...right];
}