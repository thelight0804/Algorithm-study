/*
Date:
  23.04.10
Problem:
  Programmers 12939
Project:
  최댓값과 최솟값
Level:
  Lv. 2
Author:
  thelight0804
*/

function solution(s) {
  var answer = '';
  //string array to int array
  var arr = s.split(' ')
  
  //set answer
  answer = Math.min(...arr) + " " + Math.max(...arr)
  
  return answer;
}