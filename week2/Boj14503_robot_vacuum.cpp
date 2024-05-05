#include <iostream>
#include <vector>

using namespace std;

int N, M;
int r, c, d;
vector<vector<int>> room;

// 북, 동, 남, 서 방향으로의 이동을 정의합니다.
int dx[] = {-1, 0, 1, 0};
int dy[] = {0, 1, 0, -1};

int cleanCount = 0;

void clean(int x, int y, int direction) {
    // 현재 위치를 청소합니다.
    if (room[x][y] == 0) {
        room[x][y] = 2;
        cleanCount++;
    }

    // 네 방향 모두 청소가 이미 되어있거나 벽인 경우를 확인합니다.
    int cleanable = 0;
    for (int i = 0; i < 4; ++i) {
        int nextDirection = (direction + 3 - i) % 4;
        int nx = x + dx[nextDirection];
        int ny = y + dy[nextDirection];

        if (nx >= 0 && nx < N && ny >= 0 && ny < M) {
            if (room[nx][ny] == 0) {
                cleanable++;
            }
        }
    }

    // 네 방향 모두 청소가 되어있거나 벽인 경우 후진합니다.
    if (cleanable == 0) {
        int nextDirection = (direction + 2) % 4;
        int nx = x + dx[nextDirection];
        int ny = y + dy[nextDirection];

        if (nx >= 0 && nx < N && ny >= 0 && ny < M) {
            if (room[nx][ny] != 1) {
                clean(nx, ny, direction);
            }
        }
    }
    // 청소 가능한 경우를 우선적으로 찾아 이동합니다.
    else {
        int nextDirection = (direction + 3 - cleanable) % 4;
        int nx = x + dx[nextDirection];
        int ny = y + dy[nextDirection];

        if (nx >= 0 && nx < N && ny >= 0 && ny < M) {
            if (room[nx][ny] == 0) {
                clean(nx, ny, nextDirection);
            }
        }
    }
}

int main() {
    cin >> N >> M;
    cin >> r >> c >> d;

    room.resize(N, vector<int>(M));

    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < M; ++j) {
            cin >> room[i][j];
        }
    }

    clean(r, c, d);

    cout << cleanCount << endl;

    return 0;
}
