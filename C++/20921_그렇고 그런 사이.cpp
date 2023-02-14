#include <iostream>
#include <vector>

using namespace std;

vector<int> input_seq;
vector<int> head;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    int N, K;
    cin >> N >> K;

    for (int i = 1; i < N + 1; i++) {
        input_seq.push_back(i);
    }

    int n = N - 1;
    while (K) {
        if (K >= n) {
            K -= n;
            head.push_back(n + 1);
            input_seq[n] = 0;
        }
        n -= 1;
    }

    for (int i = 0; i < head.size(); i++) {
        cout << head[i] << ' ';
    }
    for (int i = 0; i < input_seq.size(); i++) {
        if (input_seq[i])
            cout << input_seq[i] << ' ';
    }
}