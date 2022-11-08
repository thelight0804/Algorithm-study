/**
 * @author thelight0804 <br>
 * Date: 2022.08.07 <br>
 * Title: Programmers 알고리즘 문제 해설 1번 <br>
 * Project: 자릿수 더하기 <br>
 */
package Programmers;

class Num01 {
  public boolean solution(int[] arr) {
    boolean answer = true;
    int arrLen = arr.length; //array 길이
    int[] check = new int[arrLen]; //체크 array

    //array 숫자 체크
    for(int i=0; i<arrLen; i++){
      int num = arr[i];
      if(arrLen < num){
        answer = false;
        break;
      }
      else
        check[num-1] = 1;
    }
    return answer;
  }
}