package class01;
import java.util.Scanner;
/**
 * @author thelight0804<br>
 * Date: 2022.05.18<br>
 * Title: BAEKJOON 10869번 <br>
 * Project: 사칙연산 <br>
 * Level: Bronze 5 <br>
 * 제출 시 class 이름을 Main으로 변경해야 한다
 */
public class Num10869 {
    public static void main(String args[]) {
        //문자열 입력
        Scanner sc = new Scanner(System.in);
        String str = sc.nextLine();

        //" " 기준으로 문자열을 배열로 분리
        String strs[] = str.split(" ");

        //분리한 문자열을 각 int로 변환
        int a = Integer.parseInt(strs[0]);
        int b = Integer.parseInt(strs[1]);

        //사칙연산 수행
        System.out.println(a+b); //+ 연산
        System.out.println(a-b); //- 연산
        System.out.println(a*b); //* 연산
        System.out.println(a/b); //몫 연산
        System.out.println(a%b); //나머지 연산
    }
}

