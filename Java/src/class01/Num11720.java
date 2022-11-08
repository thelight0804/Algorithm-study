package class01;

import java.util.Scanner;

/**
 * @author thelight0804<br>
 * Date: 2022.05.23<br>
 * Title: BAEKJOON 11720번 <br>
 * Project: 숫자의 합 <br>
 * Level: Bronze 2 <br>
 * 제출 시 class 이름을 Main으로 변경해야 한다
 */
public class Num11720 {
    public static void main(String args[]) {
        int sum = 0; //덧셈 결과

        //숫자의 개수 입력
        Scanner sc = new Scanner(System.in);
        String count = sc.nextLine();
        int countNum = Integer.parseInt(count);

        //합할 숫자 입력
        char[] numArr = sc.nextLine().toCharArray();

        //숫자 덧셈
        for(int i=0; i < countNum; i++)
            sum += Character.getNumericValue(numArr[i]);

        //결과 출력
        System.out.println(sum);
    }
}

