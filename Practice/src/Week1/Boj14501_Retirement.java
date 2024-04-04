package Week1;

import java.util.*;
import java.io.*;

// 14501번 문제
public class Boj14501_Retirement {

    public static void main(String[] args) throws IOException{

        int N; // 전체 날 개수

        int duration[]; // 상담 기간

        int cost[]; // 비용

        int max = 0; // 벌 수 있는 가장 높은 비용

        int totalList[];

        int temp = 0; // 비교를 위한 temp

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); // 입력 받기 위한 버퍼 리더
        StringBuilder sb = new StringBuilder(); // 출력을 위한 스트링 빌더

        N = Integer.parseInt(br.readLine()); // 전체 날을 입력받고

        //해당 날 만큼 배열을 생성
        duration = new int[N];
        cost = new int[N];
        totalList = new int[N];


        // 날만큼 비용과 기간을 입력 받기
        for (int i = 0; i < N; i++){
            StringTokenizer stringTokenizer = new StringTokenizer(br.readLine());
            duration[i] = Integer.parseInt(stringTokenizer.nextToken()); // 기간
            cost[i] = Integer.parseInt(stringTokenizer.nextToken()); // 비용
        }

        for(int i = 0; i < N; i++){ // 최대 수익들을 저장한 배열을 생성
            totalList[i] = getTotal(i, N, duration, cost);
        }

        for(int i = 0; i < N; i++){ // 최대값 찾기
            if (max < totalList[i]){
                max = totalList[i];
            }
        }

        System.out.println(max);

        for (int i = 0; i < N; i++){
            System.out.print(duration[i] + " ");
        }
        System.out.println();
        for (int i = 0; i < N; i++){
            System.out.print(cost[i] + " ");
        }
        System.out.println();
        for (int i = 0; i < N; i++){
            System.out.print(totalList[i] + " ");
        }
    }

    // i번째 날에서 시작해서 얻을 수 있는 최대 수익을 재귀적으로 저장
    public static int getTotal(int i, int N, int duration[], int cost[]){
        int temp = 0;
        if(duration[i] + i < N + 1){
            temp += cost[i]; // 비용 더하기
            i = duration[i] + i; // 다음 상담 날짜
            if(i != N) {
                temp += getTotal(i, N, duration, cost); //재귀적으로 호출해서 상담 기간 후 또 발생하는 비용을 추가
            }
        }
        return temp; //임시 가격들을 반환
    }

}