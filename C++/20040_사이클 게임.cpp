#include <iostream>
#include <vector>

using namespace std;

int N, M;
int parent[500001];
int _rank[500001];
vector<int> result;

int find(int a) {
    if (parent[a] == a)
        return a;

    return parent[a] = find(parent[a]);
}

bool vnion(int a, int b) {
    a = find(a);
    b = find(b);

    if (a == b)
        return true;

    if (_rank[a] > _rank[b]) {
        parent[b] = a;
        _rank[a]++;
    } else {
        parent[a] = b;
        _rank[b]++;
    }

    return false;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    cin >> N >> M;
    for (int i = 0; i < N; i++)
        parent[i] = i;

    int a, b;
    for (int i = 1; i <= M; i++) {
        cin >> a >> b;
        if (vnion(a, b))
            result.push_back(i);
    }

    cout << (result.empty() ? 0 : result.front());

    return 0;
}