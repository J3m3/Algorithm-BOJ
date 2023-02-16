#include <iostream>

using namespace std;

#define MAX 40000001

int V, E;
int u, v, w;
int result = MAX;

int main() {
    ios_base::sync_with_stdio(false);
    cout.tie(nullptr);
    cin.tie(nullptr);

    cin >> V >> E;
    int graph[V][V];
    fill(&graph[0][0], &graph[V - 1][V], MAX);

    for (int i = 0; i < E; i++) {
        cin >> u >> v >> w;
        graph[u - 1][v - 1] = w;
    }

    for (int m = 0; m < V; m++) {
        for (int i = 0; i < V; i++) {
            for (int j = 0; j < V; j++) {
                graph[i][j] = min(graph[i][j], graph[i][m] + graph[m][j]);
            }
        }
    }

    for (int i = 0; i < V; i++) {
        result = min(result, graph[i][i]);
    }

    cout << (result == MAX ? -1 : result);
}