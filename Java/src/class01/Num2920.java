/*
Date : 22.05.10
Title : BAEKJOON 2920번
Project : 음계
Level : Bronze 2
Name : thelight0804
제출 시 class 이름을 Main으로 변경해야 한다
*/

package class01;

import java.util.Scanner;

public class Num2920 {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        char[] chs = sc.nextLine().toCharArray();
        boolean ascending = false;
        boolean descending = false;
        int note = 1; //음표

        //ascending Check
        for (int i = 0; i < chs.length; i += 2) {
            //Character.getNumericValue(Char) = Char to Int
            if (note == Character.getNumericValue(chs[i]))
                ascending = true;
            else {
                ascending = false;
                break; //하나라도 틀리면 빠져 나간다
            }
            note += 1;
        }

        //descending Check
        note = 8;
        for (int i = 0; i < chs.length; i += 2) {
            if (note == Character.getNumericValue(chs[i]))
                descending = true;
            else {
                descending = false;
                break; //하나라도 틀리면 빠져 나간다
            }
            note -= 1;
        }

        //result print
        if (ascending)
            System.out.println("ascending");
        else if (descending)
            System.out.println("descending");
        else
            System.out.println("mixed");
    }
}
