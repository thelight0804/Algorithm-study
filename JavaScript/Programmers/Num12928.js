/*
Date:
  23.04.06
Problem:
  Programmers 12928
Project:
  약수의 합
Level:
  Lv. 1
Author:
  thelight0804
*/

//if-else
function solution(n) {
  var sum = 0;
  
  for(var i = 1; i < n+1; i++)
      if (n % i == 0) sum += i;
  
  return sum;
}

//Ternary operator
function solution(n) {
  var sum = 0
  
  for(var i = 1; i < n+1; i++)
      n % i == 0 ? sum += i : null
  
  return sum
}
