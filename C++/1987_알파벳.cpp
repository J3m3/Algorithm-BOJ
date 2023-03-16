#include <iostream>
#include <queue>
#include <string>
#include <utility>

using namespace std;

int R, C, maximum;
char board[21][21];
int char_visited[26];
int dx[4] = {0, 0, 1, -1};
int dy[4] = {1, -1, 0, 0};

void dfs(int y, int x, int depth) {
    maximum = max(depth, maximum);
    for (int i = 0; i < 4; i++) {
        int ny = y + dy[i];
        int nx = x + dx[i];

        if (!(0 <= nx && nx < C && 0 <= ny && ny < R))
            continue;

        if (char_visited[board[ny][nx] - 'A'])
            continue;

        char_visited[board[ny][nx] - 'A'] = 1;
        dfs(ny, nx, depth + 1);
        char_visited[board[ny][nx] - 'A'] = 0;
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    cin >> R >> C;
    for (int y = 0; y < R; y++)
        for (int x = 0; x < C; x++)
            cin >> board[y][x];

    char_visited[board[0][0] - 'A'] = 1;
    dfs(0, 0, 1);

    cout << maximum;

    return 0;
}
