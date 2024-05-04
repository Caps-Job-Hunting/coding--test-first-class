#include <iostream>
#include <vector>
#include <string>

using namespace std;

// 1. gear N,S 입력.
// 2. rotation 회전 여부 판단.
// 3. rotation 회전 로직.

vector<int> gears[4];

void rotate(int gear, int direction) {
    if (direction == 1) {
        int temp = gears[gear][7];
        gears[gear].pop_back();
        gears[gear].insert(gears[gear].begin(), temp);
    } else {
        int temp = gears[gear][0];
        gears[gear].erase(gears[gear].begin());
        gears[gear].push_back(temp);
    }
}


void rotateGears(int gear, int direction) {
    int rotations[4] = {0};
    rotations[gear] = direction;

    for (int i = gear - 1; i >= 0; i--) {
        if (gears[i][2] != gears[i + 1][6]) {
            rotations[i] = -rotations[i + 1];
        } else {
            break;
        }
    }

    for (int i = gear + 1; i < 4; i++) {
        if (gears[i - 1][2] != gears[i][6]) {
            rotations[i] = -rotations[i - 1];
        } else {
            break;
        }
    }

    for (int i = 0; i < 4; i++) {
        if (rotations[i] != 0) {
            rotate(i, rotations[i]);
        }
    }
}

int main() {
    for (int i = 0; i < 4; i++) {
        string gear;
        cin >> gear;
        for (char c : gear) {
            gears[i].push_back(c - '0');
        }
    }

    int K;
    cin >> K;
    for (int i = 0; i < K; i++) {
        int gear, direction;
        cin >> gear >> direction;
        rotateGears(gear - 1, direction);
    }

    int score = 0;
    for (int i = 0; i < 4; i++) {
        if (gears[i][0] == 1) {
            score += (1 << i);
        }
    }

    cout << score << endl;

    return 0;
}
