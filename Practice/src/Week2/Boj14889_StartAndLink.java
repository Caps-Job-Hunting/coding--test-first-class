package Week2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Boj14889_StartAndLink {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    static StringTokenizer st;

    static int N;
    static int[][] abilities;

    public static void main (String[] args) throws IOException{
        N = Integer.parseInt(br.readLine());
        abilities = new int[N][N];

        for(int i = 0; i < N; i++){
            st = new StringTokenizer(br.readLine());
            for(int j = 0; j < N; j++) {
                abilities[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        boolean[][] visited = new boolean[N][N];
        for(int i = 0; i < N/2; i++){
            dfs(i, i + 1, visited);
        }

        for(int i = 0; i < visited.length; i++) {
            System.out.println(visited[i]);
        }
    }

    static void dfs (int n, int d, boolean[][] visited){
        if(n == N/2){
            return;
        }
        visited[n][n+1] = true;
        System.out.println("visited : " + n + " " + visited[n]);
        dfs(n, d+1, visited);
        visited[n][n] = false;
    }

}

