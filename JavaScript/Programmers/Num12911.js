/*
Date:
  23.04.18
Problem:
  Programmers 12911
Project:
  다음 큰 숫자
Level:
  Lv. 2
Author:
  thelight0804
*/

////use function
/**
 * 숫자를 2진수로 변환하여 1의 개수를 반환한다
 * @param {number} a 2진수로 변환할 숫자
 * @returns 변환된 2진수의 1의 개수
 */
function countOne(a){
  var binary = a.toString(2).split('');
  var count = 0; //1 count
  for(var i = 0; i < binary.length; i++){
      if (binary[i] === '1') count ++;
  }
  return count;
}

function solution(n) {
  var answer = n;

  //add number + 1
  while(true){
      answer ++;
       //check same 1 count
      if(countOne(n) === countOne(answer))
          return answer;
  }
}

////use split('1')
function solution(n) {
  //count 1 by Binary
  var oneN = n.toString(2).split('1').length;
  var answer = n;

  while(true){
      answer ++; //add + 1
      countAnswer = answer.toString(2).split('1').length;
      if(oneN === countAnswer) //check same 1 count
          return answer;
  }
}