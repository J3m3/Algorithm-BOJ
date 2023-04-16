#include <iostream>
#include <queue>
#include <vector>

using namespace std;

int N, M;
vector<int> tree[1002];
int dist[1002][1002];

int bfs(int s, int t) {
    queue<int> q;
    int visited[1002] = {0};
    q.push(s);
    visited[s] = 1;

    while (!q.empty()) {
        int cur = q.front();
        if (cur == t)
            return visited[cur] - 1;

        q.pop();
        for (int nxt : tree[cur])
            if (!visited[nxt]) {
                q.push(nxt);
                visited[nxt] = visited[cur] + dist[cur][nxt];
            }
    }
    return -1;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    cin >> N >> M;
    for (int i = 0; i < N - 1; i++) {
        int u, v, w;
        cin >> u >> v >> w;
        tree[u].push_back(v);
        tree[v].push_back(u);
        dist[u][v] = w;
        dist[v][u] = w;
    }

    for (int i = 0; i < M; i++) {
        int u, v;
        cin >> u >> v;
        cout << bfs(u, v) << '\n';
    }

    return 0;
}
