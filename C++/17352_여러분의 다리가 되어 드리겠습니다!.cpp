#include <iostream>

using namespace std;

int N, u, v;
int parent[300002];

int find(int a) {
    if (parent[a] == a)
        return a;
    return parent[a] = find(parent[a]);
}

void vnion(int a, int b) {
    a = find(a);
    b = find(b);

    if (a == b)
        return;

    if (a > b)
        swap(a, b);

    parent[b] = a;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    cin >> N;
    for (int i = 1; i < N + 1; i++)
        parent[i] = i;

    for (int i = 0; i < N - 2; i++) {
        cin >> u >> v;
        vnion(u, v);
    }

    for (int i = 1; i < N + 1; i++)
        find(i);

    for (int i = 2; i < N + 1; i++)
        if (parent[i - 1] != parent[i]) {
            cout << parent[i - 1] << " " << parent[i];
            break;
        }
    return 0;
}
