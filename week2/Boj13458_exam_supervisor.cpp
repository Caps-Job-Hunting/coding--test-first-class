#include <iostream>
#include <vector>

using namespace std;

// 1. n개의 시험장, A_i명의 응시자
// 2. 총감독관 1명 ; B명의 응시자관리, 부감독관 many ; C명의 응시자관리
// 3. i=ALL, 모든 A_i명의 응시자 관리에 필요한, 감독관들 최소 인원을 구하라.

typedef long long ll;

int main(){

    ll n, i, result;
    vector<int> A;
    ll B, C;
    int gen_super=0, dep_super=0;

    cin >> n;

    int tmp;
    for (i = 0; i < n; i++){
        cin >> tmp;
        A.push_back(tmp);
    }

    cin >> B >> C;

    // main logic
    for (i = 0; i < n; i++){
        tmp = A[i];
        if(tmp <= B)
            gen_super++;
        else{
            int tmp2 = tmp - B;
            gen_super++;
            dep_super += tmp2 % C ? tmp2 / C + 1 : tmp2 / C;
        }
    }
    result = gen_super + dep_super;

    cout << result << '\n';

    return 0;
}
