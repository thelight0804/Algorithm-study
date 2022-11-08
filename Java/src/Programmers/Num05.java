/**
 * @author thelight0804 <br>
 * Date: 2022.09.28 <br>
 * Title: Programmers 알고리즘 문제 해설 5번 <br>
 * Project: 땅따먹기 <br>
 */
package Programmers;

class Num05 {
  int solution(int[][] land) {
    int answer = 0; //답

    for(int i=0; i < land.length -1; i++){ //한 행씩 반복
      //다음 행에 현재 요소중 가장 큰 값을 더하면서 내려간다
      land[i+1][0] += Math.max(Math.max(land[i][1], land[i][2]), land[i][3]);
      land[i+1][1] += Math.max(Math.max(land[i][0], land[i][2]), land[i][3]);
      land[i+1][2] += Math.max(Math.max(land[i][0], land[i][1]), land[i][3]);
      land[i+1][3] += Math.max(Math.max(land[i][0], land[i][1]), land[i][2]);

      //행의 요소 중 가장 큰 값을 answer에 넣는다
      answer = Math.max(Math.max(land[i+1][0], land[i+1][1]), Math.max(land[i+1][2], land[i+1][3]));
    }
    return answer;
  }
}