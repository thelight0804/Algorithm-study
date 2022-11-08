/**
 * @author thelight0804<br>
 * Date: 2022.09.07<br>
 * Title: BAEKJOON 9625번 <br>
 * Project: BABBA <br>
 * Level: Silver 5 <br>
 * 제출 시 class 이름을 Main으로 변경해야 한다
 */

package BAEKJOON;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Num9625 {
  static int [] dp = new int [46];
  public static void main(String args[]) throws IOException {
    //test 입력
    BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
    int test = Integer.parseInt(bf.readLine());

    int b = AB(test);
    int a = dp[test-1];

    //a의 예외상황
    if (test == 1)
      a = 0;
    else if (test == 2 || test == 3)
      a = 1;

    System.out.println(a + " " + b);
  }

  //피보나치를 이용한 재귀함수
  static int AB (int test){
    if (test == 1)
      return 1;
    if (test == 2)
      return 1;
    if (dp[test] == 0)
      dp[test] = AB(test-1) + AB(test - 2);
    return dp[test];
  }
}