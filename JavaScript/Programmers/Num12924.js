/*
Date:
  23.04.16
Problem:
  Programmers 12924
Project:
  숫자의 표현
Level:
  Lv. 2
Author:
  thelight0804
*/
function solution(n) {
  var cnt = new Array(n+1).fill(0); //count array 1
  
  for(var i = 1; i < n+1; i++){ //2
      var sum = 0; //3
      for(var j = i; j < n+1; j++){ //accumulate sum 4
          sum += j;
          if(sum > n) break; //5
          else cnt[sum] += 1; // add cnt 6
      }
  }
  
  //output result
  return cnt[n];
}