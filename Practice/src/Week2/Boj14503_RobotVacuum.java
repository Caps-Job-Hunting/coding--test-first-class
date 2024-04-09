package Week2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Boj14503_RobotVacuum {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    static StringTokenizer st;

    static int N;
    static int M;

    static int r;
    static int c;

    static int d; // 방향
    static int count = 0; // 청소한 위치 개수
    static boolean end = true; // 작동 유무
    static int[][] room; // 방
    static int[] dX = {-1,0,1,0};
    static int[] dY = {0,1,0,-1}; // 북:0, 동:1, 서:2, 남:3


    public static void main (String[] args) throws IOException {
        //입력
        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        room = new int[N][M];

        st = new StringTokenizer(br.readLine());
        r = Integer.parseInt(st.nextToken());
        c = Integer.parseInt(st.nextToken());
        d = Integer.parseInt(st.nextToken());

        //벽 확인을 위한 임시 좌표
        int tempX = 0;
        int tempY = 0 ;

        for(int i = 0; i < N; i++){
            st = new StringTokenizer(br.readLine());
            for(int j = 0; j < M; j++) {
                room[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        while(end){ // 작동이 끝날때까지
            clean(r,c, room); // 1번. 현재 칸이 아직 청소되지 않은 경우, 현재 칸을 청소한다.
            if (!checkRoom(r,c, room)){//현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우,
                tempX = r + dX[(d+2) % 4]; // 후진을 위한 방향 전한
                tempY = c + dY[(d+2) % 4]; // 후진을 위한 방향 전한
                if((0 < tempX && tempX < N) && (0 < tempY && tempY < M)){ //방 안이면서
                    if(room[tempX][tempY] == 1){ //만약에 뒤에가 벽이면 이동 안함.
                        break;
                    }
                    // 바라보는 방향을 유지한 채로 한 칸 후진할 수 있다면 한 칸 후진하고 1번으로 돌아간다.
                    r = tempX;
                    c = tempY;
//                    System.out.println("Move to " + r + " " + c);
                } else { // 바라보는 방향의 뒤쪽 칸이 벽이라 후진할 수 없다면 작동을 멈춘다.
                    end = false; // 작동 중지
                }
            }else{  // 3번. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있다면,
                d = (d+3) % 4; // 반시계 방향으로 90도 회전
                tempX = r + dX[d];
                tempY = c + dY[d];
                if((0 < tempX && tempX < N) && (0 < tempY && tempY < M)){ // 회전한 방향으로 이동한 좌표가 방안이면서
                    if(room[tempX][tempY] == 0){ // 바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 빈 칸인 경우 한 칸 전진한다.
                        r += dX[d];
                        c += dY[d];
                    }
//                    System.out.println("Move to " + r + " " + c);
                }
            }
        }
        System.out.println(count);
    }

    static void clean(int x, int y, int[][] room){ // 현재 칸이 아직 청소되지 않은 경우, 현재 칸을 청소한다.
        if(room[x][y] == 0){
            room[x][y] = 2;
            count++;
//            System.out.println("Cleaned " + x + " " + y);
        }
    }

    static boolean checkRoom(int x, int y, int[][] room){ // 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는지 확인,
        int tempX = 0;
        int tempY = 0;
        boolean flag = false;
        for(int i = 0; i < 4; i++){
            tempX = x + dX[i];
            tempY = y + dY[i];
            if((0 <= tempX && tempX < N) && (0 <= tempY && tempY < M)){
               if(room[tempX][tempY] == 0){
//                   System.out.println("Not Clean Yet " + tempX + " " + tempY);
                   flag = true;
               }
            }
        }
        return flag;
    }
}
