/*
Date:
  23.04.06
Problem:
  Programmers 12944
Project:
  평균 구하기
Level:
  Lv. 1
Author:
  thelight0804
*/

function solution(arr) {
  var answer = 0;
  var sum = 0;
  
  //sum arr
  arr.forEach(e=>{
      sum += e
  })
  
  //calculate average
  answer = sum / arr.length
  
  return answer;
}