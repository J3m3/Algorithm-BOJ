#include <iostream>
#define MAX_JUMP 19 // >= log_200001

using namespace std;

int m, Q, nxt[500002][MAX_JUMP];

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    cin >> m;
    for (int i = 1; i <= m; i++)
        cin >> nxt[i][0];

    for (int j = 1; j < MAX_JUMP; j++)
        for (int i = 1; i <= m; i++)
            nxt[i][j] = nxt[nxt[i][j - 1]][j - 1];

    cin >> Q;
    for (int i = 0; i < Q; i++) {
        int n, x;
        cin >> n >> x;
        for (int j = 0; j < MAX_JUMP; j++)
            if (n & 1 << j)
                x = nxt[x][j];
        cout << x << '\n';
    }

    return 0;
}
