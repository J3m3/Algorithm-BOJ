#include <cstring>
#include <iostream>
#include <queue>
#include <utility>

using namespace std;

int N, M;
char board[51][51];
int visited[51][51];
int dx[4] = {0, 0, 1, -1};
int dy[4] = {1, -1, 0, 0};
queue<pair<int, int>> q;

int bfs() {
    int count = 0;
    while (!q.empty()) {
        int y = q.front().first;
        int x = q.front().second;
        q.pop();

        for (int i = 0; i < 4; i++) {
            int ny = y + dy[i];
            int nx = x + dx[i];

            if (!(0 <= nx && nx < M && 0 <= ny && ny < N))
                continue;

            if (visited[ny][nx])
                continue;

            if (board[ny][nx] == 'W')
                continue;

            q.push({ny, nx});
            visited[ny][nx] = visited[y][x] + 1;
            count = max(count, visited[ny][nx]);
        }
    }
    return count;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    cin >> N >> M;
    for (int i = 0; i < N; i++)
        for (int j = 0; j < M; j++)
            cin >> board[i][j];

    int count = 0;
    for (int i = 0; i < N; i++)
        for (int j = 0; j < M; j++) {
            if (board[i][j] == 'L') {
                memset(visited, 0, sizeof(visited));
                visited[i][j] = 1;
                q.push({i, j});
                count = max(count, bfs());
            }
        }
    cout << count - 1;
    return 0;
}
