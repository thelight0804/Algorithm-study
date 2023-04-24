/*
Date:
  23.04.24
Problem:
  Programmers 42842
Project:
  카펫
Level:
  Lv. 2
Author:
  thelight0804
*/

function solution(brown, yellow) {
  var sum = brown + yellow;
  var h = 3; //height
  var w = 3; //width
  
  for(; h < brown; h++){
      if(sum % h == 0){
          w = sum / h; //set width
          if((h >= sum / h) && (h-2)*(w-2) === yellow){
              return [h, w];
          }
      }
  }
}