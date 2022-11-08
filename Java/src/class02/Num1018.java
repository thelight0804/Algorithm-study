/**
 * @author thelight0804<br>
 * Date: 2022.08.04<br>
 * Title: BAEKJOON 1018번 <br>
 * Project: 체스판 다시 칠하기 <br>
 * Level: Silver 5 <br>
 * 제출 시 class 이름을 Main으로 변경해야 한다
 */

package class02;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Num1018 {
  public static void main(String args[]) throws IOException {
    //숫자 입력
    BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
    String[] str = bf.readLine().split(" ");
    int row = Integer.parseInt(str[0]); //행 (ㅡ)
    int column = Integer.parseInt(str[1]); //열 (ㅣ)

    //2차원 string 배열 선언
    String[][] Board = new String[row][column]; //기존 체스판

    for(int i=0; i<column; i++){
      String[] temp = bf.readLine().split("");
      for(int j=0; j<row; j++){
        Board[j][i] = temp[j];
      }
    }


    //틀린 횟수
    int count = 0;

  }
}
