/*
Date:
  23.04.06
Problem:
  Programmers 12954
Project:
  x만큼 간격이 있는 n개의 숫자
Level:
  Lv. 1
Author:
  thelight0804
*/

function solution(x, n) {
  var answer = [];
  for(var i = 1; i < n+1; i++)
      answer.push(i*x)
  
  return answer;
}