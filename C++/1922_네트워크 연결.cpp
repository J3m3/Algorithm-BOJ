#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

int N, M, result;
int parent[1002];
int rank_arr[1002];

int find(int a) {
    if (parent[a] == a)
        return a;
    return parent[a] = find(parent[a]);
}

bool vnion(int a, int b) {
    a = find(a);
    b = find(b);

    if (a == b)
        return false;

    if (rank_arr[a] > rank_arr[b])
        swap(a, b);

    parent[a] = b;

    if (rank_arr[a] == rank_arr[b])
        ++rank_arr[b];

    return true;
}

int main() {
    cin >> N >> M;
    vector<vector<int>> edges(M, vector<int>(3, 0));
    for (int i = 0; i < M; i++)
        for (int j = 0; j < 3; j++)
            cin >> edges[i][j];

    for (int i = 1; i <= N; i++)
        parent[i] = i;

    sort(edges.begin(), edges.end(),
         [](vector<int> &u, vector<int> &v) -> bool { return u[2] < v[2]; });

    for (vector<int> edge : edges)
        if (vnion(edge[0], edge[1]))
            result += edge[2];

    cout << result;

    return 0;
}
