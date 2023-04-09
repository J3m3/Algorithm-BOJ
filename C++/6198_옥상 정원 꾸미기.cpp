#include <iostream>
#include <stack>
#define ll long long

using namespace std;

ll N, h, arr[80002], result;
stack<ll> s;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    cin >> N;
    for (int i = 1; i < N + 1; i++) {
        cin >> h;
        arr[i] = h;
    }

    for (int i = 1; i < N + 1; i++) {
        while (!s.empty() && arr[s.top()] <= arr[i])
            s.pop();
        result += (ll)s.size();
        s.push(i);
    }

    cout << result;
    return 0;
}
