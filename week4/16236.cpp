#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#include <climits> // 이 라이브러리를 추가하여 INT_MAX를 사용할 수 있습니다.

using namespace std;

int N;
int map[20][20];
int dist[20][20];
int shark_size = 2;
int shark_eat = 0;
int shark_x, shark_y;
int dx[4] = {-1, 0, 0, 1};
int dy[4] = {0, -1, 1, 0};

void reset_dist() {
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            dist[i][j] = -1;
        }
    }
}

bool bfs() {
    queue<pair<int, int>> q;
    reset_dist();
    q.push({shark_x, shark_y});
    dist[shark_x][shark_y] = 0;

    int min_dist = INT_MAX;
    vector<pair<int, int>> fish;

    while (!q.empty()) {
        int x = q.front().first;
        int y = q.front().second;
        q.pop();

        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];

            if (nx >= 0 && nx < N && ny >= 0 && ny < N && dist[nx][ny] == -1 && map[nx][ny] <= shark_size) {
                dist[nx][ny] = dist[x][y] + 1;
                q.push({nx, ny});
                if (map[nx][ny] > 0 && map[nx][ny] < shark_size) {
                    if (dist[nx][ny] < min_dist) {
                        min_dist = dist[nx][ny];
                        fish.clear();
                        fish.push_back({nx, ny});
                    } else if (dist[nx][ny] == min_dist) {
                        fish.push_back({nx, ny});
                    }
                }
            }
        }
    }

    if (!fish.empty()) {
        sort(fish.begin(), fish.end());
        shark_x = fish[0].first;
        shark_y = fish[0].second;
        map[shark_x][shark_y] = 0;
        shark_eat++;
        if (shark_eat == shark_size) {
            shark_size++;
            shark_eat = 0;
        }
        return true;
    }
    return false;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> N;
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            cin >> map[i][j];
            if (map[i][j] == 9) {
                shark_x = i;
                shark_y = j;
                map[i][j] = 0;
            }
        }
    }

    int answer = 0;
    while (bfs()) {
        answer += dist[shark_x][shark_y];
    }

    cout << answer << '\n';
    return 0;
}
