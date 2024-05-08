#include <cstdio>		
#include <vector>		
#include <algorithm>
#include <iostream>
#include <string>
#include <map>
#include<stack>
#include<queue>
#include<cstdlib>
#include<ctime>
#include<cstring>
#include<utility>
#define prev J
const int INF = 987654321;
const int dy[] = { -1,0,1,0 };
const int dx[] = { 0,1,0,-1 };
using namespace std;
typedef long long ll;
//ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
//*point ; 비트마스킹 -> 경우의 수 탐색
//for using __builtin_popcount();
#ifdef _MSC_VER
#  include <intrin.h>
#  define __builtin_popcount __popcnt
#endif

int s[24][24], ret = INF, n;
int go(vector<int>& a, vector<int>& b) {
	pair<int, int> ret;
	for (int i = 0; i < n / 2; i++) {
		for (int j = 0; j < n / 2; j++) {
			if (i == j)continue;
			ret.first += s[a[i]][a[j]];
			ret.second += s[b[i]][b[j]];
		}
	}
	return abs(ret.first - ret.second);
}

int main() {
	cin >> n;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			cin >> s[i][j];
		}
	}
	for (int i = 0; i < (1 << n); i++) {
		//__builtin_popcount(i) ; 비트가 몇개 켜져있는지
		if (__builtin_popcount(i) != n / 2) continue; 
		vector<int> start, link;
		for (int j = 0; j < n; j++) {
			if (i & (1 << j))start.push_back(j);
			else link.push_back(j);
		}
		ret = min(ret, go(start, link));
	}
	cout << ret << "\n";
	return 0;
}





