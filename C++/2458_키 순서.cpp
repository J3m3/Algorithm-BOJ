#include <iostream>

using namespace std;

int N, M, cnt;
int graph[502][502];
int check[502];

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    cin >> N >> M;
    for (int i = 0; i < M; i++) {
        int u, v;
        cin >> u >> v;
        graph[u][v] = 1;
        graph[v][u] = -1;
        check[u] += 2;
        check[v] += 2;
    }

    for (int k = 1; k <= N; k++)
        for (int i = 1; i <= N; i++)
            for (int j = 1; j <= N; j++) {
                if (graph[i][j])
                    continue;
                if (graph[i][k] == 1 && graph[k][j] == 1) {
                    graph[i][j] = 1;
                    check[i]++;
                    check[j]++;
                } else if (graph[i][k] == -1 && graph[k][j] == -1) {
                    graph[i][j] = -1;
                    check[i]++;
                    check[j]++;
                }
            }

    for (int i = 1; i <= N; i++)
        if (check[i] == N - 1 << 1)
            cnt++;

    cout << cnt;

    return 0;
}
