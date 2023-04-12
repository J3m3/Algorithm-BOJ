#include <iostream>
#include <map>
#define ll long long

using namespace std;

int N, K;
ll psum[200002], result;
map<ll, int> m;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    cin >> N >> K;
    for (int i = 1; i <= N; i++) {
        ll t;
        cin >> t;
        psum[i] = psum[i - 1] + t;
    }

    for (int i = 1; i <= N; i++) {
        if (psum[i] == K)
            result++;
        result += m[psum[i] - K];
        m[psum[i]]++;
    }
    cout << result;
    return 0;
}
