#include <cstring>
#include <iostream>
#include <queue>
#include <utility>

using namespace std;

int w, h;
int board[51][51];
int visited[51][51];
int dx[8] = {0, 0, 1, -1, 1, -1, -1, 1};
int dy[8] = {1, -1, 0, 0, -1, 1, -1, 1};

void bfs(int x, int y) {
    queue<pair<int, int>> q;
    visited[y][x] = 1;
    q.push({y, x});

    while (!q.empty()) {
        y = q.front().first;
        x = q.front().second;
        q.pop();

        for (int i = 0; i < 8; i++) {
            int ny = y + dy[i];
            int nx = x + dx[i];

            if (!(0 <= nx && nx < w && 0 <= ny && ny < h))
                continue;

            if (visited[ny][nx])
                continue;

            if (!board[ny][nx])
                continue;

            q.push({ny, nx});
            visited[ny][nx] = 1;
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    while (1) {
        cin >> w >> h;
        if (w == 0 && h == 0)
            break;

        for (int y = 0; y < h; y++)
            for (int x = 0; x < w; x++)
                cin >> board[y][x];

        int count = 0;
        for (int y = 0; y < h; y++)
            for (int x = 0; x < w; x++)
                if (!visited[y][x] && board[y][x]) {
                    bfs(x, y);
                    count++;
                }
        cout << count << "\n";

        memset(visited, 0, sizeof(visited));
    }

    return 0;
}
