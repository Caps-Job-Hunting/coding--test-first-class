package Week1;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Boj14891_Gear {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static ArrayList<ArrayList<Integer>> gears = new ArrayList<>();

    public static void main(String[] args) throws IOException {
        // 톱니바퀴 초기화
        initializeGears();

        // 회전 명령 처리
        int rotationCount = Integer.parseInt(br.readLine());
        for (int i = 0; i < rotationCount; i++) {
            st = new StringTokenizer(br.readLine());
            int gearNum = Integer.parseInt(st.nextToken());
            int direction = Integer.parseInt(st.nextToken());

            // 톱니바퀴 회전
            rotateGear(gearNum - 1, direction, new boolean[4]);
        }

        int result = 0;
        result = calculateScore(gears);
        System.out.println(result);
    }

    // 4개의 톱니바퀴 생성 및 리스트에 추가
    static void initializeGears() throws IOException {
        for (int i = 0; i < 4; i++) {
            st = new StringTokenizer(br.readLine());
            ArrayList<Integer> gear = new ArrayList<>(); // 각 톱니 바퀴 생성
            String line = st.nextToken();
            for (int j = 0; j < line.length(); j++) {
                gear.add(Character.getNumericValue(line.charAt(j))); //입력값 저장
            }
            gears.add(gear);
        }
    }

    // 톱니바퀴 회전
    static void rotateGear(int gearIndex, int direction, boolean[] visited) {
        visited[gearIndex] = true;
        ArrayList<Integer> currentGear = gears.get(gearIndex);

        // 제일 왼쪽 톱니바퀴까지 재귀하면서 회전
        if (gearIndex > 0 && !visited[gearIndex - 1] && currentGear.get(6) != gears.get(gearIndex - 1).get(2)) {
            rotateGear(gearIndex - 1, -direction, visited);
        }

        // 제일 오른쪽 톱니바퀴까지 재귀하면서 회전
        if (gearIndex < 3 && !visited[gearIndex + 1] && currentGear.get(2) != gears.get(gearIndex + 1).get(6)) {
            rotateGear(gearIndex + 1, -direction, visited);
        }

        // 현재 톱니바퀴 회전하기
        rotate(currentGear, direction);
    }

    // 톱니바퀴 회전
    static void rotate(ArrayList<Integer> gear, int direction) {
        if (direction == 1) { // 시계 방향 회전
            int last = gear.remove(7);
            gear.add(0, last); // 마지막꺼 삭제해서 제일 처음에 추가
        } else if (direction == -1) { // 반시계 방향 회전
            int first = gear.remove(0);
            gear.add(first); // 처음꺼 삭제해서 제일 마지막에 추가
        }
    }

    // 톱니바퀴의 점수 계산
    static int calculateScore(ArrayList<ArrayList<Integer>> gears) {
        int score = 0;
        for (int i = 0; i < 4; i++) {
            ArrayList<Integer> gear = gears.get(i);
            // 12시 방향의 극을 확인하여 점수 계산
            if (gear.get(0) == 1) {
                score += Math.pow(2, i); //i 번째 톱니바퀴에 따라 제곱
            }
        }
        return score;
    }
}
