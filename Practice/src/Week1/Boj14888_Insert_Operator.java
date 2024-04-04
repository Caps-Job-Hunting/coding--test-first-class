package Week1;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

// 14888번 문제
public class Boj14888_Insert_Operator {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;

    static PriorityQueue<Long> resultQueue = new PriorityQueue<Long>(Collections.reverseOrder());

    static ArrayList<Integer> opList = new ArrayList<Integer>();

    static int N;
    static int[] numbers;
    static int[] operator;

    static int[] tempOperator;
    static boolean[] visited;

    int max = -100000000;
    int min = 100000000;

    public static void main(String[] args) throws IOException {

        N = Integer.parseInt(br.readLine());

        numbers = new int[N];
        operator = new int[N-1];
        tempOperator = new int[4];
        visited = new boolean[N-1];

        int total = 0; //총 연산자의 개수
        long numOfEquations = 0; //총 수식의 개수
        int temp = 0;


        st = new StringTokenizer(br.readLine()); // 숫자 배열 생성
        for(int i = 0; i < N; i++){
            numbers[i] = Integer.parseInt(st.nextToken());
        }

        st = new StringTokenizer(br.readLine()); // 숫자 배열 생성
        // 연산자 입력 후, 연산자 배열 생성
        int k = 0;
        for(int i = 0; i < 4; i++){
            temp = Integer.parseInt(st.nextToken());
            tempOperator[i] = temp;
            for(int j = temp; j > 0; j--){
                operator[k] = i;
                k++;
            }
        }

        for (int i : tempOperator){
            total += i;
        }

        dfs(0);

        if(resultQueue.size()==1) { // 만약에 값이 하나만 있는 경우
            resultQueue.add(resultQueue.peek()); //젤 처음 값을 복사
        }

        System.out.println(resultQueue.poll()); // 최대 값 반환 및 제거

        int size = resultQueue.size();

        for(int i=0; i<size-1; i++) {
            resultQueue.poll(); // 최소 값 제외 모든 값 반환 및 제거
        }

        System.out.println(resultQueue.poll()); // 최소 값 반환 및 제거
    }

    public static long Factorial(int num)
    {
        if (num >= 1)
            return num * Factorial(num - 1);
        else
            return 1;
    }

    public static void dfs(int depth) {

        if(depth == N-1) { //특정 연산자로 부터 특정 수식을 생성했을때, 수식 계산.

            Long answer = (long) numbers[0];

            for(int i=0; i < opList.size(); i++) {
                if(opList.get(i) == 0) { // 0 이면 +
                    answer += numbers[i+1];
                }
                else if(opList.get(i) == 1) { // 1 이면 -
                    answer -= numbers[i+1];
                }
                else if(opList.get(i) == 2) { // 2 이면 *
                    answer *= numbers[i+1];
                }
                else if(opList.get(i) == 3) { // 3 이면 /
                    answer /= numbers[i+1];
                }
            }
            if(!resultQueue.contains(answer)) { // 중복되는 값은 넣지 말자
                resultQueue.add(answer); // 중복되는 값이 없는 경우에 추가
            }
//            System.out.println("수식 생성 및 계산 완성 | 값 = " + answer);
            return;
        }

        for(int i=0; i<N-1; i++) { // 반복해서 dfs로 수식 생성
            if(!visited[i]) {
                visited[i] = true;
                opList.add(operator[i]);
//                System.out.println(operator[i]+" 추가");
                dfs(depth+1);
                opList.remove((Object)operator[i]);
//                System.out.println(operator[i]+" 제거");
                visited[i] = false;
            }
        }


    }
}


//long numerator = Factorial(total); // 분모
//long denominator = 1; //분자
//
//        for(int i = 0; i < 4; i++){
//denominator *= Factorial(tempOperator[i]);
//        }
//
//numOfEquations = numerator / denominator;
//
//        System.out.println(numOfEquations);
//
//
