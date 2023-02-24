#include <iostream>
#include <vector>

using namespace std;

int N, u, v, cur;
bool visited[1000002];
int dp[1000002][2];
vector<vector<int>> tree(1000002);

void dfs(int cur) {
    visited[cur] = true;
    dp[cur][1] = 1;
    for (int child : tree[cur]) {
        if (!visited[child]) {
            dfs(child);

            dp[cur][0] += dp[child][1];
            dp[cur][1] += min(dp[child][0], dp[child][1]);
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    cin >> N;
    for (int i = 0; i < N - 1; i++) {
        cin >> u >> v;
        tree[u].push_back(v);
        tree[v].push_back(u);
    }

    dfs(1);

    cout << min(dp[1][0], dp[1][1]);

    return 0;
}