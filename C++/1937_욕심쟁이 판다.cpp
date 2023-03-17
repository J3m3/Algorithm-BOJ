#include <iostream>

using namespace std;

int N, maximum;
int board[502][502];
int dp[502][502];
int dx[4] = {0, 0, 1, -1};
int dy[4] = {1, -1, 0, 0};

int dfs(int y, int x) {
    if (dp[y][x])
        return dp[y][x];

    for (int i = 0; i < 4; i++) {
        int ny = y + dy[i];
        int nx = x + dx[i];

        if (!(0 <= nx && nx < N && 0 <= ny && ny < N))
            continue;

        if (board[y][x] >= board[ny][nx])
            continue;

        dp[y][x] = max(dp[y][x], dfs(ny, nx) + 1);
    }
    return dp[y][x];
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    cin >> N;
    for (int y = 0; y < N; y++)
        for (int x = 0; x < N; x++)
            cin >> board[y][x];

    for (int y = 0; y < N; y++)
        for (int x = 0; x < N; x++)
            maximum = max(maximum, dfs(y, x));

    cout << maximum + 1;

    return 0;
}
