package class01;
import java.util.Scanner;
import java.util.ArrayList;
/**
 * @author thelight0804<br>
 * Date: 2022.05.21<br>
 * Title: BAEKJOON 10952번 <br>
 * Project: A+B - 5 <br>
 * Level: Bronze 3 <br>
 * 제출 시 class 이름을 Main으로 변경해야 한다
 */
public class Num10952 {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        //ArrayList 선언
        ArrayList<Integer> numArray = new ArrayList<>();

        //반복
        while (true) {
            //두 수 입력
            int a = sc.nextInt();
            int b = sc.nextInt();

            //0 0 입력 판단
            if(a == 0 && b == 0)
                break;
            else
                //결과 값 ArrayList에 추가
                numArray.add(a + b);
        } //while() End

        //결과 출력
        for (int i = 0; i < numArray.size(); i++)
            System.out.printf("%d", numArray.get(i));
    }
}

