#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>
using namespace std;

int n;
vector<int> nums;
int op[4];
int maxValue = INT_MIN, minValue = INT_MAX;

void solve(int idx, int result) {
    if (idx == n) {
        maxValue = max(maxValue, result);
        minValue = min(minValue, result);
        return;
    }
    if (op[0] > 0) {
        op[0]--;
        solve(idx + 1, result + nums[idx]);
        op[0]++;
    }
    if (op[1] > 0) {
        op[1]--;
        solve(idx + 1, result - nums[idx]);
        op[1]++;
    }
    if (op[2] > 0) {
        op[2]--;
        solve(idx + 1, result * nums[idx]);
        op[2]++;
    }
    if (op[3] > 0) {
        op[3]--;
        solve(idx + 1, result / nums[idx]);
        op[3]++;
    }
}

int main() {
    cin >> n;
    nums.resize(n);
    for (int i = 0; i < n; i++) {
        cin >> nums[i];
    }
    for (int i = 0; i < 4; i++) {
        cin >> op[i];
    }
    solve(1, nums[0]);
    cout << maxValue << '\n' << minValue;
    return 0;
}
