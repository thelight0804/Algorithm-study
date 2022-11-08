/**
 * @author thelight0804<br>
 * Date: 2022.07.13<br>
 * Title: BAEKJOON 2609번 <br>
 * Project: 최대공약수와 최소공배수 <br>
 * Level: Bronze 1 <br>
 * 제출 시 class 이름을 Main으로 변경해야 한다
 */

package class02;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Num2609 {
  public static void main(String args[]) throws IOException {
    BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
    String[] str = bf.readLine().split(" ");
    int a = Integer.parseInt(str[0]);
    int b = Integer.parseInt(str[1]);

  //최대공약수 구하기
    int i = a, k = a, j = b;
    while(k != 0){
      k = i % j;
      i = j;
      j = k;
    }
  int greatest = i;

  //최소공배수 구하기
  int least = a * b / greatest;

    System.out.println(greatest);
    System.out.println(least);
  }
}