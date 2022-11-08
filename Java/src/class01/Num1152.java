/*
Date : 22.03.31
Title : BAEKJOON 1152번
Project : 단어의 개수
Level : Bronze 2
Name : thelight0804
제출 시 class 이름을 Main으로 변경해야 한다
*/

package class01;
import java.util.Scanner;

public class Num1152 {
    public static void main(String args[]){
        //입력
        Scanner sc = new Scanner(System.in);
        String text = sc.nextLine();

        //연산
        int count = text.length(); //글자 수
        int wordNum = 0; //문장 수

        for(int i=1; i<count; i++){
            if(text.charAt(i) == ' ')
                wordNum++;
        } //for문 끝

        if(text.charAt(count-1) != ' ') //문자열 끝에 공백있을 시
            wordNum+=1;
        System.out.println(wordNum);
    }
}
