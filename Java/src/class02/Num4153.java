/**
 * @author thelight0804<br>
 * Date: 2022.07.04<br>
 * Title: BAEKJOON 4153번 <br>
 * Project: 직각삼각형 <br>
 * Level: Bronze 3 <br>
 * 제출 시 class 이름을 Main으로 변경해야 한다
 */

package class02;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.lang.Math;

public class Num4153 {
    public static void main(String args[]) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        ArrayList<String> triangles = new ArrayList<>();

        while (true) {
            //변 길이 입력 후 int array로 변환
            String[] str = bf.readLine().split(" ");
            Integer[] num = new Integer[str.length];
            for (int i = 0; i < num.length; i++)
                num[i] = Integer.parseInt(str[i]);

            //변 길이를 크기순으로 정렬
            Arrays.sort(num);

            //0, 0, 0 입력 시 종료
            if(num[0] == 0 && num[1] == 0 && num[2] == 0)
                break;

            //직각삼각형 판별
            boolean triangle = false;

            if (Math.pow(num[0], 2) + Math.pow(num[1], 2) == Math.pow(num[2], 2))
                triangle = true;

            //판정 결과 저장
            if (triangle)
                System.out.println("right");
            else
                System.out.println("wrong");
        } //while End
    }
}

