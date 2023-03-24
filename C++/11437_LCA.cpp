#include <iostream>
#include <vector>

using namespace std;

int N, M;
int parent[50002];
int depth[50002];
vector<int> tree[50002];

void dfs(int root, int d) {
    depth[root] = d;
    for (int child : tree[root])
        if (!depth[child]) {
            parent[child] = root;
            dfs(child, d + 1);
        }
}

int lca(int u, int v) {
    if (depth[u] < depth[v])
        swap(u, v);

    while (depth[u] != depth[v])
        u = parent[u];

    while (u != v) {
        u = parent[u];
        v = parent[v];
    }
    return u;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    cin >> N;
    for (int i = 0; i < N - 1; i++) {
        int u, v;
        cin >> u >> v;
        tree[u].push_back(v);
        tree[v].push_back(u);
    }

    dfs(1, 1);

    cin >> M;
    for (int i = 0; i < M; i++) {
        int u, v;
        cin >> u >> v;
        cout << lca(u, v) << '\n';
    }

    return 0;
}
