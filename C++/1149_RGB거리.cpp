#include <iostream>

using namespace std;

int N, a, b, c;
int dp[1000][3];

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    cin >> N;
    for (int i = 0; i < N; i++) {
        cin >> a >> b >> c;
        dp[i][0] = a;
        dp[i][1] = b;
        dp[i][2] = c;
    }

    for (int i = 1; i < N; i++) {
        dp[i][0] += min(dp[i - 1][1], dp[i - 1][2]);
        dp[i][1] += min(dp[i - 1][0], dp[i - 1][2]);
        dp[i][2] += min(dp[i - 1][0], dp[i - 1][1]);
    }

    int minimum = 1000 * 1000;
    for (int i = 0; i < 3; i++) {
        minimum = min(minimum, dp[N - 1][i]);
    }

    cout << minimum;
}