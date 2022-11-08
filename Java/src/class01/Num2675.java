/*
Date : 22.05.05
Title : BAEKJOON 2675번
Project : 문자열 반복
Name : thelight0804
Level : Bronze 2
제출 시 class 이름을 Main으로 변경해야 한다
*/

package class01;
import java.util.Scanner;

public class Num2675 {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int num = Integer.parseInt(sc.nextLine()); //반복 횟수

        for(int i=0;i<num;i++){
            String input = sc.nextLine();
            int index = input.indexOf(" "); //공백 구분
            int reNum = Integer.parseInt(input.substring(0, index)); //반복 횟수
            String str = input.substring(index+1, input.length()); //String형 단어
            char[] chs = str.toCharArray(); //String to Char Array

            for(int j=0; j<chs.length; j++) {
                for (int k = 0; k < reNum; k++)
                    System.out.print(chs[j]);
            }
            System.out.println(); //줄 바꿈
        }
    }
}
