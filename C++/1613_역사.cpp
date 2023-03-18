#include <iostream>

using namespace std;

int N, K, S;
int board[402][402];

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    cin >> N >> K;
    for (int i = 0; i < K; i++) {
        int u, v;
        cin >> u >> v;
        board[u][v] = -1;
        board[v][u] = 1;
    }

    for (int via = 1; via <= N; via++)
        for (int u = 1; u <= N; u++)
            for (int v = 1; v <= N; v++) {
                if (board[u][v])
                    continue;
                if (board[u][via] == 1 && board[via][v] == 1)
                    board[u][v] = 1;
                else if (board[u][via] == -1 && board[via][v] == -1)
                    board[u][v] = -1;
            }

    cin >> S;
    for (int i = 0; i < S; i++) {
        int u, v;
        cin >> u >> v;
        cout << board[u][v] << '\n';
    }

    return 0;
}
