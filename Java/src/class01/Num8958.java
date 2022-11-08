/*
Date : 22.05.10
Title : BAEKJOON 8958번
Project : OX퀴즈
Level : Bronze 2
Name : thelight0804
제출 시 class 이름을 Main으로 변경해야 한다
*/

package class01;
import java.util.Scanner;

public class Num8958 {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int repeat = Integer.parseInt(sc.nextLine()); //반복 횟수

        for(int i=0; i<repeat; i++){
            int score = 0; //총 점수
            char[] chs = sc.nextLine().toCharArray();
            //STR.toCharArray() : String to Char Array

            //char 연산
            for(int j=0; j<chs.length; j++) {
                int plusScore = 0; //연속 점수
                if (chs[j] == 'O') { //O가 발견 되면
                    for (int k = j; chs[k] != 'X'; k++) {
                        plusScore += 1;
                        if (k == chs.length-1) //끝이 X가 아닌 경우 방지
                            break;
                    }
                    score += plusScore;
                } //for( j<chs.length ) End
            }
            System.out.println(score); //다음 입력 구분
        } //for( i<repeat ) End
    }
}
