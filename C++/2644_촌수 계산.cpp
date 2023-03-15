#include <cstring>
#include <iostream>
#include <queue>
#include <vector>

using namespace std;

int n, u, v, m;
queue<int> q;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    cin >> n;
    cin >> u >> v;
    cin >> m;
    vector<vector<int>> vec(n + 1);
    int visited[n + 1];
    memset(visited, 0, sizeof(visited));

    for (int i = 0; i < m; i++) {
        int a, b;
        cin >> a >> b;
        vec[a].push_back(b);
        vec[b].push_back(a);
    }

    q.push(u);
    visited[u] = 1;

    while (!q.empty()) {
        int cur = q.front();
        q.pop();

        for (int child : vec[cur]) {
            if (!visited[child]) {
                q.push(child);
                visited[child] = visited[cur] + 1;
            }
        }
    }

    cout << (visited[v] ? visited[v] - 1 : -1);
    return 0;
}
