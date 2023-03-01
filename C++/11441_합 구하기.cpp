#include <iostream>

using namespace std;

int N, M, total, a, b;
int arr[100002];
int pref[100002];

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0), cout.tie(0);

    cin >> N;
    for (int i = 1; i <= N; i++)
        cin >> arr[i];

    for (int i = 0; i <= N; i++) {
        total += arr[i];
        pref[i] = total;
    }

    cin >> M;
    for (int i = 0; i < M; i++) {
        cin >> a >> b;
        cout << pref[b] - pref[a - 1] << '\n';
    }

    return 0;
}