/**
 * @author thelight0804<br>
 * Date: 2022.08.31<br>
 * Title: BAEKJOON 2784번 <br>
 * Project: 피보나치 수 2 <br>
 * Level: Bronze 5 <br>
 * 제출 시 class 이름을 Main으로 변경해야 한다
 */

package BAEKJOON;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Num1018{
  public static void main(String args[]) throws IOException {
    //num input
    BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
    int num = Integer.parseInt(bf.readLine());

    //memoization
    long memory[] = new long[91];
    memory[1] = 1;

    //Fibonacci
    for(int i=2;i<num+1;i++)
      memory[i] = memory[i - 1] + memory[i - 2];

    System.out.println(memory[num]);
  }
}
