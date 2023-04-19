/*
Date:
  23.04.19
Problem:
  Programmers 12945
Project:
  피보나치 수
Level:
  Lv. 2
Author:
  thelight0804
*/

////use new Array, BigInt
function solution(n) {
  //memoization
  var f = new Array(n + 1).fill(BigInt(0));
  for (var i = 1; i < n + 1; i++) {
    //set fixed number
    if (i === 1) f[i] = BigInt(1);
    //Dynamic Algorithm
    else f[i] = BigInt(f[i - 1]) + BigInt(f[i - 2]);
  }
  return f[n] % BigInt(1234567);
}


////use Array.push()
function solution(n) {
  //memoization
  var f = [];

  for (var i = 0; i < n + 1; i++) {
    //set fixed number
    if (i === 0) f.push(0);
    else if (i === 1) f.push(1);
    else {
      //Dynamic Algorithm
      var sum = f[i - 1] + f[i - 2];
      f.push((f[i - 1] + f[i - 2]) % 1234567);
    }
  }

  return f[n];
}
