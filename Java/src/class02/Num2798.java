/**
 * @author thelight0804<br>
 * Date: 2022.07.06<br>
 * Title: BAEKJOON 2798번 <br>
 * Project: 블랙잭 <br>
 * Level: Bronze 3 <br>
 * 제출 시 class 이름을 Main으로 변경해야 한다
 */

package class02;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Num2798 {
    public static void main(String args[]) throws IOException {
        //카드 수 / 정답 입력
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        String[] str = bf.readLine().split(" ");
        int cardNum = Integer.parseInt(str[0]); //카드 개수
        int answer = Integer.parseInt(str[1]); //정답

        String[] inputCards = bf.readLine().split(" "); //제시한 카드 입력
        int[] Cards = new int[inputCards.length]; //int형 카드 array


        //String to int
        for (int i = 0; i < inputCards.length; i++)
            Cards[i] = Integer.parseInt(inputCards[i]);

        int minCompare = answer; //정답과 차이값
        int compare = 0; //정답과 차이값 임시저장
        int sum = 0; //결과값 임시저장
        int result = 0; //결과값

        //블랙잭 연산
        for(int i = 0; i < Cards.length-2; i++){
            for(int j = i+1; j < Cards.length-1; j++){
                for(int k=j+1; k < Cards.length; k++){
                    sum = Cards[i] + Cards[j] + Cards[k];
                    //정답과 차이값 계산
                    compare = answer - sum;
                    if (compare < 0 && compare <= minCompare){
                        minCompare = compare;
                        result = sum;
                    }
                }
            }
        }

        //print result
        System.out.println(result);
    }
}

