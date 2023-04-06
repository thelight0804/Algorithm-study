/*
Date:
  23.04.06
Problem:
  Programmers 12937
Project:
  짝수와 홀수
Level:
  Lv. 1
Author:
  thelight0804
*/

//if-else
function solution(num) {
  if(num % 2 === 0)
      return "Even"
  else
      return "Odd"
}

//Ternary operator
function solution(num) {
  return (num % 2 === 0) ? "Even" : "Odd"
}
