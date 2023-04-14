/*
Date:
  23.04.14
Problem:
  Programmers 70129
Project:
  이진 변환 반복하기
Level:
  Lv. 2
Author:
  thelight0804
*/

function solution(s) {
  var cnt = [0, 0] //1
  
  while(s !== '1'){
      cnt[0] += 1;
      //remove 0 2
      s = s.replace(/0/g, function(x){
          cnt[1] += 1; 
          return '';
      }).length.toString(2); //convert binary code
  }
  
  return cnt;
}