#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const int INF = 987654321;

const int dx[] = {0, 1, 0, -1}; // 동, 남, 서, 북
const int dy[] = {1, 0, -1, 0};

int N, M;
vector<vector<int>> office;
vector<pair<int, int>> cctv;

// 감시 영역을 체크하는 함수
void check(int x, int y, int dir) {
    dir %= 4; // 방향을 0부터 3까지로 제한

    int nx = x, ny = y;
    while (true) {
        nx += dx[dir];
        ny += dy[dir];

        if (nx < 0 || nx >= N || ny < 0 || ny >= M || office[nx][ny] == 6) break; // 벽을 만나면 종료
        if (office[nx][ny] != 0) continue; // 이미 감시되는 곳이면 스킵

        office[nx][ny] = -1; // 감시 영역 표시
    }
}

// CCTV의 모든 방향을 조합하여 최소 사각 지대 크기를 계산하는 함수
int calcMinBlindSpot(int index) {
    if (index == cctv.size()) {
        // 모든 CCTV의 방향을 결정한 경우 사각 지대 크기 계산
        int cnt = 0;
        for (int i = 0; i < N; ++i) {
            for (int j = 0; j < M; ++j) {
                if (office[i][j] == 0) cnt++;
            }
        }
        return cnt;
    }

    int minSpot = INF;
    int x = cctv[index].first;
    int y = cctv[index].second;
    int type = office[x][y];

    for (int d = 0; d < 4; ++d) {
        vector<vector<int>> tmp = office; // 현재 office 상태를 저장

        // CCTV의 종류에 따라 감시 영역을 체크
        if (type == 1) {
            check(x, y, d);
        } else if (type == 2) {
            check(x, y, d);
            check(x, y, d + 2);
        } else if (type == 3) {
            check(x, y, d);
            check(x, y, d + 1);
        } else if (type == 4) {
            check(x, y, d);
            check(x, y, d + 1);
            check(x, y, d + 2);
        } else if (type == 5) {
            check(x, y, d);
            check(x, y, d + 1);
            check(x, y, d + 2);
            check(x, y, d + 3);
        }

        minSpot = min(minSpot, calcMinBlindSpot(index + 1));

        office = tmp; // 이전 office 상태로 복구
    }

    return minSpot;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> N >> M;

    office.resize(N, vector<int>(M));
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < M; ++j) {
            cin >> office[i][j];
            if (office[i][j] >= 1 && office[i][j] <= 5) {
                cctv.push_back({i, j});
            }
        }
    }

    int answer = calcMinBlindSpot(0);
    cout << answer << endl;

    return 0;
}
