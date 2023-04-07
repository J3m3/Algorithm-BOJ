#include <deque>
#include <iostream>

using namespace std;

int N;
deque<int> d;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    cin >> N;
    for (int i = 1; i < N + 1; i++)
        d.push_back(i);

    while (!d.empty()) {
        cout << d[0] << " ";
        d.pop_front();
        d.push_back(d.front());
        d.pop_front();
    }

    return 0;
}
