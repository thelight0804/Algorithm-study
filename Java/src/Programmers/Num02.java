/**
 * @author thelight0804 <br>
 * Date: 2022.08.11 <br>
 * Title: Programmers 알고리즘 문제 해설 2번 <br>
 * Project: 순열 검사 <br>
 */
package Programmers;
import java.util.Arrays;

class Num02 {
  public boolean solution(int[] arr) {
    boolean answer = true;

    //배열 정렬
    Arrays.sort(arr);

    //중복 확인
    for(int i=0; i < arr.length; i++){
      if(arr[i] != i+1){
        answer = false;
        break;
      }
    }

    return answer;
  }
}