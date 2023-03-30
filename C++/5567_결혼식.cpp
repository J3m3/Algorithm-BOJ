#include <iostream>
#include <vector>

using namespace std;

int N, M;
int visited[502];
vector<vector<int>> graph(502);

void dfs(int s, int depth) {
    if (depth == 2)
        return;
    for (int nxt : graph[s]) {
        visited[nxt] = 1;
        dfs(nxt, depth + 1);
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    cin >> N >> M;
    for (int i = 0; i < M; i++) {
        int u, v;
        cin >> u >> v;
        graph[u].push_back(v);
        graph[v].push_back(u);
    }

    visited[1] = 1;
    dfs(1, 0);

    int cnt = 0;
    for (int i = 1; i <= N; i++)
        if (visited[i])
            cnt++;
    cout << cnt - 1;
    return 0;
}
