/**
 * @author thelight0804 <br>
 * Date: 2022.07.27 <br>
 * Title: BAEKJOON 11650번 <br>
 * Project: 좌표 정렬하기 <br>
 * Level: Silver 5 <br>
 * 제출 시 class 이름을 Main으로 변경해야 한다
 */

package class02;

import java.io.*;
import java.util.Arrays;
import java.util.Scanner;

public class Num11650 {
  public static void main(String args[]) throws IOException {
    Scanner sc = new Scanner(System.in);

    //점의 개수 입력
    int test = 0; //점의 개수
    test = sc.nextInt();

    //좌표 정보 입력
    int coord[][] = new int[test][2]; //좌표 정보
    for(int i=0; i < test; i++) {
      coord[i][0] = sc.nextInt();
      coord[i][1] = sc.nextInt();
    }

    //Lambda식 정렬
    Arrays.sort(coord, (a, b) -> {
      if(a[0]==b[0])
        return a[1] - b[1];
      else
        return a[0] - b[0];
    });

    //출력
    BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    for(int i=0; i< coord.length; i++) {
      bw.write(coord[i][0] + " " + coord[i][1]);
      bw.write("\n");
    }
    bw.flush();
    bw.close();
  }
}