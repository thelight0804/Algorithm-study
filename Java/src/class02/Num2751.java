/**
 * @author thelight0804 <br>
 * Date: 2022.07.21 <br>
 * Title: BAEKJOON 1181번 <br>
 * Project: 수 정렬하기 2 <br>
 * Level: Silver 5 <br>
 * 제출 시 class 이름을 Main으로 변경해야 한다
 */

package class02;

import java.io.*;
import java.util.Arrays;

public class Num2751 {
  public static void main(String args[]) throws IOException {
    //입력 받기
    BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
    int count = Integer.parseInt(bf.readLine()); //입력 횟수
    int num[] = new int[count];
    //숫자 입력
    for(int i=0; i<count; i++)
      num[i] = Integer.parseInt(bf.readLine());

    //수 정렬하기
    Arrays.sort(num);
    
    //출력하기
    ////BufferedWriter를 사용하여 출력 시간 단축
    BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    for(int i=0; i<num.length; i++)
      bw.write(num[i] + "\n");
    bw.flush();
    bw.close();
  }
}