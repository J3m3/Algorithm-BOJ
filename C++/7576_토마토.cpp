#include <iostream>
#include <queue>
#include <utility>

using namespace std;

int M, N;
int board[1001][1001];
queue<pair<int, int>> q;
int dx[4] = {0, 0, 1, -1};
int dy[4] = {1, -1, 0, 0};

int check_board() {
    int result = 0;
    for (int y = 0; y < N; y++) {
        for (int x = 0; x < M; x++) {
            if (board[y][x] == 0)
                return -1;

            result = max(result, board[y][x]);
        }
    }

    return result - 1;
}

void bfs() {
    while (!q.empty()) {
        int x = q.front().first;
        int y = q.front().second;
        q.pop();

        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];

            if (!((0 <= nx && nx < M) && (0 <= ny && ny < N)))
                continue;

            if (board[ny][nx] != 0)
                continue;

            q.push({nx, ny});
            board[ny][nx] = board[y][x] + 1;
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    cin >> M >> N;

    for (int y = 0; y < N; y++) {
        for (int x = 0; x < M; x++) {
            cin >> board[y][x];
            if (board[y][x] == 1) {
                q.push({x, y});
            }
        }
    }

    bfs();
    cout << check_board();

    return 0;
}