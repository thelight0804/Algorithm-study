/*
Date : 22.04.06
Title : BAEKJOON 1330번
Project : 두 수 비교하기
Level : Bronze 4
Name : thelight0804
제출 시 class 이름을 Main으로 변경해야 한다
*/

package class01;

import java.util.Scanner;

public class Num1330 {
    public static void main(String args[]){
        //입력
        Scanner sc = new Scanner(System.in);
        String num = sc.nextLine();

        //빈 칸 구분
        int index = num.indexOf(" ");

        int a =  Integer.parseInt(num.substring(0, index)); //첫 번째 수 추출
        
        //단순히 index값으로 추출하면 10자리 이상 수를 구하지 못한다
        ///int a =  Character.getNumericValue(num.charAt(0));
        ///Character.getNumericValue : Char to int
        ///Str.charAt(Num) : Str index(Num)을 Char로 반환

        int b =  Integer.parseInt(num.substring(index+1, num.length())); //두 번째 수 추출

        //a,b 연산
        if(a>b)
            System.out.println(">");
        else if (a<b)
            System.out.println("<");
        else
            System.out.println("==");
    }
}
