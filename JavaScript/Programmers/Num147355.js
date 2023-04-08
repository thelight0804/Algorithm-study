/*
Date:
  23.04.08
Problem:
  Programmers 147355
Project:
  크기가 작은 부분문자열
Level:
  Lv. 1
Author:
  thelight0804
*/

function solution(t, p) {
  var answer = 0;
  
  //set length
  var len_t = t.length;
  var len_p = p.length;
  
  //t slice
  for(var i = 0; i < (len_t-len_p+1); i++){
      var num = t.slice(i, i+len_p);
      //add count
      if(num <= p) answer++;
  }
  
  return answer;
}