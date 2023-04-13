/*
Date:
  23.04.13
Problem:
  Programmers 12941
Project:
  최솟값 만들기
Level:
  Lv. 2
Author:
  thelight0804
*/

//for
function solution(A,B){
  var answer = 0;
  
  //sort array 1
  A.sort((a, b) => a - b);
  B.sort((a, b) => a - b);
  
  //add multiple 2
  for(var i = 0; i < A.length; i++){
      answer += A[i] * B[B.length-i-1]; //3
  }

  return answer;
}

//reduce
function solution(A,B){
  var answer = 0;
  
  //sort array
  A.sort((a, b) => a - b);
  B.sort((a, b) => b - a);
  
  return A.reduce((acc, cur, idx) => acc += cur * B[idx], 0)
}