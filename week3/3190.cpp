#include <iostream>
#include <queue>
#include <vector>

using namespace std;

const int dx[] = {0, 1, 0, -1}; // 동, 남, 서, 북
const int dy[] = {1, 0, -1, 0};

int N, K, L;
int board[101][101]; // 보드의 크기는 최대 100x100이므로 101x101로 선언
vector<pair<int, char>> directions; // 방향 전환 정보

int changeDirection(int dir, char c) {
    if (c == 'L') return (dir + 3) % 4; // 왼쪽으로 90도 회전
    else return (dir + 1) % 4; // 오른쪽으로 90도 회전
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> N >> K;
    for (int i = 0; i < K; ++i) {
        int x, y;
        cin >> x >> y;
        board[x][y] = 1; // 사과가 있는 위치는 1로 표시
    }

    cin >> L;
    for (int i = 0; i < L; ++i) {
        int X;
        char C;
        cin >> X >> C;
        directions.push_back({X, C});
    }

    int dir = 0; // 초기 방향은 동쪽(오른쪽)
    int time = 0;
    int x = 1, y = 1;
    queue<pair<int, int>> snake;
    snake.push({x, y});
    board[x][y] = 2; // 뱀의 머리는 2로 표시

    int idx = 0;
    while (true) {
        // 방향 전환 시간일 때 방향 전환
        if (idx < directions.size() && directions[idx].first == time) {
            dir = changeDirection(dir, directions[idx].second);
            idx++;
        }

        // 머리 이동
        x += dx[dir];
        y += dy[dir];
        time++;

        // 벽 또는 자기 자신의 몸과 부딪히면 게임 종료
        if (x < 1 || x > N || y < 1 || y > N || board[x][y] == 2) break;

        // 사과가 없으면 꼬리를 당김
        if (board[x][y] != 1) {
            int nx = snake.front().first;
            int ny = snake.front().second;
            snake.pop();
            board[nx][ny] = 0; // 꼬리 제거
        }

        snake.push({x, y});
        board[x][y] = 2; // 머리 표시
    }

    cout << time << '\n';

    return 0;
}
