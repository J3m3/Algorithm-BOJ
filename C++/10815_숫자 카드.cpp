#include <iostream>
#include <set>

using namespace std;

int N, M;
set<int> s;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    cin >> N;
    for (int i = 0; i < N; i++) {
        int n;
        cin >> n;
        s.insert(n);
    }

    cin >> M;
    for (int i = 0; i < M; i++) {
        int n;
        cin >> n;
        if (s.find(n) != s.end())
            cout << 1 << " ";
        else
            cout << 0 << " ";
    }
    return 0;
}
