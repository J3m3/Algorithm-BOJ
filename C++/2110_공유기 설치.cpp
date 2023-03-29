#include <algorithm>
#include <iostream>
#include <vector>
#define ll long long

using namespace std;

ll N, C, l, r;
vector<ll> coords;

ll check(ll mid) {
    ll cnt = 1;
    ll prev = coords[0];
    for (int i = 1; i < N; i++)
        if (coords[i] - prev >= mid) {
            cnt++;
            prev = coords[i];
        }
    return cnt;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    cin >> N >> C;
    for (int i = 0; i < N; i++) {
        ll coord;
        cin >> coord;
        coords.push_back(coord);
    }
    sort(coords.begin(), coords.end());

    l = 1;
    r = coords[N - 1] - coords[0] + 1;
    while (l < r) {
        ll mid = (l + r) / 2;
        ll cnt = check(mid);

        if (cnt >= C)
            l = mid + 1;
        else
            r = mid;
    }
    cout << l - 1;
    return 0;
}
