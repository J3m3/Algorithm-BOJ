#include <iostream>

using namespace std;
#define fastio ios_base::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
#define MAX 15

int N;
int count = 0;
int coords[MAX];

bool IsPromising(int idx) {
    for (int i = 0; i < idx; i++) {
        if (coords[i] == coords[idx])
            return 0;

        if (idx - i == abs(coords[idx] - coords[i]))
            return 0;
    }
    return 1;
}

void DFS(int idx) {
    if (idx == N) {
        count++;
        return;
    }
    for (int i = 0; i < N; i++) {
        coords[idx] = i;
        if (IsPromising(idx))
            DFS(idx+1);
    }
}

int main() {
    fastio;

    cin >> N;
    DFS(0);
    cout << count;

    return 0;
}