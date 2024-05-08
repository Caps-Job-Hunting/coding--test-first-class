#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
using namespace std;

//혼자서 못품.

struct Tree {
    int x, y, age;
    bool alive;
};

int N, M, K;
int A[10][10], nutrients[10][10];
vector<Tree> trees;
int dx[8] = {-1, -1, -1, 0, 0, 1, 1, 1};
int dy[8] = {-1, 0, 1, -1, 1, -1, 0, 1};

bool comp(Tree &a, Tree &b) {
    return a.age < b.age;
}

void springAndSummer() {
    for (auto &tree : trees) {
        if (tree.alive) {
            if (nutrients[tree.x][tree.y] >= tree.age) {
                nutrients[tree.x][tree.y] -= tree.age;
                tree.age++;
            } else {
                tree.alive = false;
                nutrients[tree.x][tree.y] += tree.age / 2;
            }
        }
    }
}

void autumn() {
    vector<Tree> newTrees;
    for (auto &tree : trees) {
        if (tree.alive && tree.age % 5 == 0) {
            for (int i = 0; i < 8; i++) {
                int nx = tree.x + dx[i];
                int ny = tree.y + dy[i];
                if (nx >= 0 && nx < N && ny >= 0 && ny < N) {
                    newTrees.push_back({nx, ny, 1, true});
                }
            }
        }
    }
    trees.insert(trees.end(), newTrees.begin(), newTrees.end());
}

void winter() {
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            nutrients[i][j] += A[i][j];
        }
    }
}

int main() {
    cin >> N >> M >> K;
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            cin >> A[i][j];
            nutrients[i][j] = 5; 
        }
    }

    int x, y, age;
    for (int i = 0; i < M; i++) {
        cin >> x >> y >> age;
        trees.push_back({x - 1, y - 1, age, true});
    }

    sort(trees.begin(), trees.end(), comp);

    for (int year = 0; year < K; year++) {
        springAndSummer();
        autumn();
        winter();
    }

    int aliveTrees = 0;
    for (auto &tree : trees) {
        if (tree.alive) aliveTrees++;
    }

    cout << aliveTrees << endl;
    return 0;
}
