#include <iostream>
#include <vector>

using namespace std;

int main() {
    int N, M, x, y, K;
    cin >> N >> M >> x >> y >> K;

    vector<vector<int>> map(N, vector<int>(M));
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < M; ++j) {
            cin >> map[i][j];
        }
    }

    vector<int> commands(K);
    for (int i = 0; i < K; ++i) {
        cin >> commands[i];
    }

    int dice[6] = {0}; // 주사위의 상태를 나타내는 배열
    int dx[] = {0, 0, -1, 1}; // 동, 서, 북, 남
    int dy[] = {1, -1, 0, 0};

    for (int cmd : commands) {
        int nx = x + dx[cmd - 1];
        int ny = y + dy[cmd - 1];

        if (nx < 0 || nx >= N || ny < 0 || ny >= M) continue;

        // 주사위 상태를 업데이트
        int temp;
        switch (cmd) {
            case 1: // 동쪽
                temp = dice[0];
                dice[0] = dice[3];
                dice[3] = dice[5];
                dice[5] = dice[2];
                dice[2] = temp;
                break;
            case 2: // 서쪽
                temp = dice[0];
                dice[0] = dice[2];
                dice[2] = dice[5];
                dice[5] = dice[3];
                dice[3] = temp;
                break;
            case 3: // 북쪽
                temp = dice[0];
                dice[0] = dice[1];
                dice[1] = dice[5];
                dice[5] = dice[4];
                dice[4] = temp;
                break;
            case 4: // 남쪽
                temp = dice[0];
                dice[0] = dice[4];
                dice[4] = dice[5];
                dice[5] = dice[1];
                dice[1] = temp;
                break;
        }

        if (map[nx][ny] == 0) {
            map[nx][ny] = dice[5];
        } else {
            dice[5] = map[nx][ny];
            map[nx][ny] = 0;
        }

        cout << dice[0] << '\n';

        x = nx;
        y = ny;
    }

    return 0;
}
