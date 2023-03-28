#include <cstring>
#include <iostream>
#include <queue>
#include <vector>

using namespace std;

int L, R, C;
char board[32][32][32];
int visited[32][32][32];
vector<int> sp(3), ep(3);

int dx[] = {0, 0, 1, -1, 0, 0};
int dy[] = {1, -1, 0, 0, 0, 0};
int dz[] = {0, 0, 0, 0, 1, -1};

int bfs(int sz, int sy, int sx) {
    memset(visited, 0, sizeof(visited));
    visited[sz][sy][sx] = 1;

    queue<vector<int>> q;
    q.push(sp);

    while (!q.empty()) {
        int z = q.front()[0];
        int y = q.front()[1];
        int x = q.front()[2];
        q.pop();

        if (z == ep[0] && y == ep[1] && x == ep[2])
            return visited[z][y][x] - 1;

        for (int i = 0; i < 6; i++) {
            int nz = z + dz[i];
            int ny = y + dy[i];
            int nx = x + dx[i];

            if (!(0 <= nx && nx < C && 0 <= ny && ny < R && 0 <= nz && nz < L))
                continue;

            if (board[nz][ny][nx] == '#')
                continue;

            if (visited[nz][ny][nx])
                continue;

            visited[nz][ny][nx] = visited[z][y][x] + 1;
            q.push({nz, ny, nx});
        }
    }
    return -1;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    while (1) {
        cin >> L >> R >> C;
        if (L == 0 && R == 0 && C == 0)
            return 0;
        for (int z = 0; z < L; z++) {
            for (int y = 0; y < R; y++)
                for (int x = 0; x < C; x++) {
                    cin >> board[z][y][x];
                    if (board[z][y][x] == 'S') {
                        sp[0] = z;
                        sp[1] = y;
                        sp[2] = x;
                    } else if (board[z][y][x] == 'E') {
                        ep[0] = z;
                        ep[1] = y;
                        ep[2] = x;
                    }
                }
        }
        int result = bfs(sp[0], sp[1], sp[2]);
        if (result >= 0)
            cout << "Escaped in " << result << " minute(s)." << '\n';
        else
            cout << "Trapped!" << '\n';
    }
    return 0;
}
