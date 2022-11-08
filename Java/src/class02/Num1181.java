/**
 * @author thelight0804<br>
 * Date: 2022.07.18<br>
 * Title: BAEKJOON 1181번 <br>
 * Project: 단어 정렬 <br>
 * Level: Silver 5 <br>
 * 제출 시 class 이름을 Main으로 변경해야 한다
 */

package class02;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Comparator;

public class Num1181 {
  public static void main(String args[]) throws IOException {
    int count = 0; //단어의 개수 저장

    //입력 받기
    BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
    count = Integer.parseInt(bf.readLine());
    String[] words = new String[count];

    //단어 개수 만큼 단어 입력
    for (int i = 0; i < count; i++) {
      String word = bf.readLine();
      words[i] = word;
    }

    //ArrayList 정렬하기
    Arrays.sort(words, new Comparator<String>() {
      @Override
      public int compare(String a, String b) {
        if (a.length() == b.length())
          return a.compareTo(b);
        else
          return a.length() - b.length();
      }
    });


    //words print
    System.out.println(words[0]);
    for (int i = 1; i < count; i++) {
      if(!words[i].equals(words[i-1]))
        System.out.println(words[i]);
    }
  }
}