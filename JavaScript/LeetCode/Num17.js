/*
Date:
  23.04.26
Number:
  LeetCode 1710
Title:
  Maximum Units on a Truck
Level:
  Easy
Author:
  thelight0804
*/

/**
 * @param {number[][]} boxTypes
 * @param {number} truckSize
 * @return {number}
 */
var maximumUnits = function(boxTypes, truckSize) {
  var units = 0;
  boxTypes.sort((a, b) => b[1] - a[1] ); //sort boxTypes

  //loop box
  for(var i = 0; i < boxTypes.length; i++){
		//truck is full
    if(truckSize <= 0) return units;
		//can put all unit in truck
    if(truckSize > boxTypes[i][0]){
      units += boxTypes[i][0] * boxTypes[i][1]
      truckSize -= boxTypes[i][0]
    }
    else{ //can put part of in truck
      units += boxTypes[i][1] * truckSize;
      truckSize -= boxTypes[i][0]
    }
  }
  return units;
};