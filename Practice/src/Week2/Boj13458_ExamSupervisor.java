package Week2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Boj13458_ExamSupervisor {
    static int N = 0; // 총 시험장 수
    static int A[]; // 총 응시자 수
    static int B = 0; // 총감독관이 관리하는 응시자 수
    static int C = 0; // 부감독관이 관리하는 응시자 수
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        init();
        long totalNum = 0;
        totalNum = calculateMin();
        System.out.println(totalNum);
    }

    public static void init() throws IOException {

        N = Integer.parseInt(br.readLine());
        A = new int[N];

        if(N == 1){
            A[0] = Integer.parseInt(br.readLine());
        }else{
            st = new StringTokenizer(br.readLine());
            for(int i = 0; i < N; i++){
                A[i] = Integer.parseInt(st.nextToken());
            }
        }
        st = new StringTokenizer(br.readLine());

        B = Integer.parseInt(st.nextToken());

        C = Integer.parseInt(st.nextToken());
    }

    public static long calculateMin(){
        long totalCountOfHeadSuperv = 0; // 총감독관의 수
        long totalCountOfSubSuperv = 0; // 부감독관의 수

        long tempCountOfHeadSuperv; // 총감독관의 수
        long tempCountOfSubSuperv; // 부감독관의 수

        int temp;
        for(int i = 0; i < N; i++){

            //변수 초기화
            temp = 0;
            tempCountOfHeadSuperv = 0;
            tempCountOfSubSuperv = 0;

            if (A[i] <= B){ // 만약 총감독관 보다 수가 작다면 그냥 한명 추가 후 다음 강의실 확인
                totalCountOfHeadSuperv++;
                continue;
            }else{ // 아니라면 총감독관 만큼 뺀 학생들을 위해 몇 명이 필요한지 나누기로 구함
                temp = A[i] - B;
                tempCountOfHeadSuperv++;
                tempCountOfSubSuperv = temp / C;
                if(temp % C != 0)
                    tempCountOfSubSuperv++;
            }

            //최종 값 계산
            totalCountOfHeadSuperv += tempCountOfHeadSuperv;
            totalCountOfSubSuperv += tempCountOfSubSuperv;

        }

        //반환
        return totalCountOfSubSuperv + totalCountOfHeadSuperv;
    }


}
