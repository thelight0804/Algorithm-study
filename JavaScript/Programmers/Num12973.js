/*
Date:
  23.04.22
Problem:
  Programmers 12973
Project:
  짝지어 제거하기
Level:
  Lv. 2
Author:
  thelight0804
*/

function solution(s)
{   
    //check s.length odd number
    if(s.length % 2 === 1) return 0;
 
    var stack = []; //stack
    
    for(var item of s){
        //pop
        if(item === stack[stack.length-1]) stack.pop();
        //push
        else stack.push(item);
    }
    //check result
    return stack.length === 0 ? 1 : 0;
}