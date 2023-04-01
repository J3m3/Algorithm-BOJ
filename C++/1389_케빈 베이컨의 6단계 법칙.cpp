#include <cstring>
#include <iostream>
#include <queue>
#include <vector>

using namespace std;

int N, M;
vector<int> graph[102];
int visited[102];

int bfs(int s) {
    queue<int> q;
    q.push(s);
    memset(visited, 0, sizeof(visited));
    visited[s] = 1;

    while (!q.empty()) {
        int cur = q.front();
        q.pop();
        for (int nxt : graph[cur])
            if (!visited[nxt]) {
                q.push(nxt);
                visited[nxt] = visited[cur] + 1;
            }
    }
    int sum = 0;
    for (int i = 1; i < N + 1; i++)
        if (i != s)
            sum += visited[i];
    return sum;
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

    int result = 0;
    int minimum = 6000;
    for (int i = 1; i < N + 1; i++) {
        int t = bfs(i);
        if (t < minimum) {
            minimum = t;
            result = i;
        }
    }
    cout << result;
    return 0;
}
