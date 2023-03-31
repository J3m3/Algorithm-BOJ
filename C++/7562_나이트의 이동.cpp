#include <iostream>
#include <queue>
#include <utility>

using namespace std;

int T, N, x, y, tx, ty;
int board[302][302];
int dx[8] = {1, 2, 2, 1, -1, -2, -2, -1};
int dy[8] = {2, 1, -1, -2, -2, -1, 1, 2};

int bfs(int sy, int sx) {
    queue<pair<int, int>> q;
    int visited[302][302] = {0};
    q.push({y, x});
    visited[y][x] = 1;

    while (!q.empty()) {
        int y = q.front().first;
        int x = q.front().second;
        q.pop();
        if (y == ty && x == tx)
            return visited[ty][tx] - 1;

        for (int i = 0; i < 8; i++) {
            int ny = y + dy[i];
            int nx = x + dx[i];

            if (!(0 <= nx && nx < N && 0 <= ny && ny < N))
                continue;

            if (visited[ny][nx])
                continue;

            visited[ny][nx] = visited[y][x] + 1;
            q.push({ny, nx});
        }
    }
    return -1;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    cin >> T;
    for (int i = 0; i < T; i++) {
        cin >> N >> y >> x >> ty >> tx;
        cout << bfs(y, x) << '\n';
    }
    return 0;
}
