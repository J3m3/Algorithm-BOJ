#include <iostream>
#include <queue>

using namespace std;

int N, s, e, U, D, visited[1000002];
queue<int> q;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    cin >> N >> s >> e >> U >> D;

    q.push(s);
    visited[s] = 1;
    while (!q.empty()) {
        int cur = q.front();
        q.pop();
        if (cur == e) {
            cout << visited[cur] - 1;
            return 0;
        }
        for (int next : {cur + U, cur - D})
            if (0 < next && next <= N && !visited[next]) {
                q.push(next);
                visited[next] = visited[cur] + 1;
            }
    }
    cout << "use the stairs";
    return 0;
}
