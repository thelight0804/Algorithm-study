/*
Date:
  23.04.06
Problem:
  Programmers 12931
Project:
  자릿수 더하기
Level:
  Lv. 1
Author:
  thelight0804
*/

function solution(n)
{
    var answer = 0;
		
		//number to string array
    var arr = n.toString().split('');
    
    //sum Array
    arr.forEach(e=>{
        answer += parseInt(e)
    })
    
    return answer;
}