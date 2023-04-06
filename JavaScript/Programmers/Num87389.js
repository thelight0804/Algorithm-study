/*
Date:
  23.04.06
Problem:
  Programmers 87389
Project:
  나머지가 1이 되는 수 찾기
Level:
  Lv. 1
Author:
  thelight0804
*/

function solution(n) {
  for(var i = 0; i < n; i++){
      if(n % i === 1) return i
  }
}