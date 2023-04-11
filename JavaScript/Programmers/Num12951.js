/*
Date:
  23.04.11
Problem:
  Programmers 12951
Project:
  JadenCase 문자열 만들기
Level:
  Lv. 2
Author:
  thelight0804
*/

//for
function solution(s) {
  //split stirng
  s = s.split(' ')
  
  //loop string array
  for(var i = 0; i < s.length; i++){
      if(s[i].length != 0) //check blank ' '
          s[i] = s[i][0].toUpperCase() + s[i].slice(1, s[i].length).toLowerCase();
  }
  
  //combine stirng array
  return s.join(' ');
}

//map
function solution(s) {
  return s
    .split(" ") //split stirng
    .map((e) => e.charAt(0).toUpperCase() + e.substring(1).toLowerCase())
    .join(" "); //combine stirng array
}