/*
Date:
  23.04.07
Problem:
  Programmers 42748
Project:
  K번째수
Level:
  Lv. 1
Author:
  thelight0804
*/

function solution(array, commands) {
  var answer = [];
  
  commands.forEach(e=>{
      //set i, j, k
      var i = e[0] - 1
      var j = e[1]
      var k = e[2] - 1
      
      //slice Array and sort
      sliceArr = array.slice(i, j).sort((a, b)=>a - b)
      console.log(sliceArr)
      
      //add answer
      answer.push(sliceArr[k])
  })
  
  return answer;
}