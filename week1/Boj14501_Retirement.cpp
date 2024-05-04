#include <iostream>
#include <vector>
using namespace std;

int n, answer = 0;
vector<int> T, P;

void solve(int day, int sum) {
    if (day == n) { // 퇴사일 도달
        answer = max(answer, sum);
        return;
    }
    if (day > n) { // 퇴사일 Over
        return;
    }
    solve(day + T[day], sum + P[day]); // 상담 Yes
    solve(day + 1, sum); // 상담 No
}

int main() {
    cin >> n;
    int t, p;
    for (int i = 0; i < n; i++) {
			cin >> t>> p;
			T.push_back(t); P.push_back(p);
    }
    solve(0, 0);
    cout << answer;
    return 0;
}