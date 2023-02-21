#include <iostream>
#include <queue>
#include <vector>

using namespace std;

int N, M, v, infected, cur, child;
vector<vector<int>> graph(200002);
vector<int> distances(200002, -1);
int infect_left[200002];
queue<int> q;

void bfs() {
    while (!q.empty()) {
        cur = q.front();
        q.pop();
        for (size_t i = 0; i < graph[cur].size(); i++) {
            child = graph[cur][i];
            if (distances[child] == -1) {

                infect_left[child]--;
                if (infect_left[child] <= 0) {
                    q.push(child);
                    distances[child] = distances[cur] + 1;
                }
            }
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    cin >> N;
    for (int u = 1; u <= N; u++) {
        vector<int> list;
        while (1) {
            cin >> v;
            if (v == 0)
                break;
            list.push_back(v);
        }
        graph[u] = list;
    }

    cin >> M;
    for (int i = 0; i < M; i++) {
        cin >> infected;
        q.push(infected);
        distances[infected] = 0;
    }

    for (int i = 1; i <= N; i++)
        infect_left[i] = (graph[i].size() + 1) / 2;

    bfs();

    for (int i = 1; i <= N; i++)
        cout << distances[i] << ' ';

    return 0;
}