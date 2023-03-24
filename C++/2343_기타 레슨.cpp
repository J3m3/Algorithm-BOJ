#include <iostream>
#define ll long long

using namespace std;

ll N, M, low, high, b_size;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    cin >> N >> M;
    ll lectures[N];
    for (int i = 0; i < N; i++) {
        cin >> lectures[i];
        low = max(low, lectures[i]) - 1;
        high += lectures[i];
    }

    while (low + 1 < high) {
        b_size = (low + high) / 2;
        ll total = 0;
        ll b_cnt = 1;
        for (int i = 0; i < N; i++) {
            if (total + lectures[i] > b_size) {
                b_cnt++;
                total = 0;
            }
            total += lectures[i];
        }
        if (b_cnt <= M)
            high = b_size;
        else
            low = b_size;
    }
    cout << high;
    return 0;
}
