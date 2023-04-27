/*
Date:
  23.04.27
Problem:
  Programmers 42885
Project:
  구명보트
Level:
  Lv. 2
Author:
  thelight0804
*/

function solution(people, limit) {
  //descending sort
  people.sort((a, b) => b - a);
  var count = 0;
  
  //check two people can boat
  for(var right = 0, left = people.length - 1; right <= left; right++){
      if(people[right] + people[left] <= limit) left --; //can two people
      count ++; //add boat count
  }

  return count;
}