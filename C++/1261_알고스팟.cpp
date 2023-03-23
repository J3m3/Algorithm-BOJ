#include <deque>
#include <iostream>
#include <string>
#include <utility>

using namespace std;

int N, M;
int maze[101][101];
int visited[101][101];
int dx[4] = {0, 0, 1, -1};
int dy[4] = {1, -1, 0, 0};
deque<pair<int, int>> d;

void bfs() {
    while (!d.empty()) {
        int x = d.front().first;
        int y = d.front().second;
        d.pop_front();

        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];

            if (!(0 <= nx && nx < M && 0 <= ny && ny < N))
                continue;
            if (visited[ny][nx])
                continue;

            if (maze[ny][nx]) {
                d.push_back({nx, ny});
                visited[ny][nx] = visited[y][x] + 1;

            } else {
                d.push_front({nx, ny});
                visited[ny][nx] = visited[y][x];
            }
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    cin >> M >> N;
    for (int i = 0; i < N; i++) {
        string line;
        cin >> line;
        for (int j = 0; j < M; j++)
            maze[i][j] = line[j] - '0';
    }

    visited[0][0] = 1;
    d.push_back({0, 0});
    bfs();

    cout << visited[N - 1][M - 1] - 1;
    return 0;
}
