#include <iostream>
#define ll long long

using namespace std;

int N;
ll dist[100002];
ll price[100002];
ll now, total;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    cin >> N;
    for (int i = 1; i < N; i++)
        cin >> dist[i];

    for (int i = 0; i < N; i++)
        cin >> price[i];

    now = price[0];
    total += now * dist[1];

    for (int i = 1; i < N; i++) {
        if (now > price[i])
            now = price[i];
        total += now * dist[i + 1];
    }

    cout << total;

    return 0;
}
