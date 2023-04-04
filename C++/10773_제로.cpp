#include <iostream>
#include <numeric>
#include <vector>

using namespace std;

int K, n;
vector<int> stack;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    cin >> K;
    for (int i = 0; i < K; i++) {
        cin >> n;
        if (n == 0) {
            stack.pop_back();
            continue;
        }
        stack.push_back(n);
    }
    cout << accumulate(stack.begin(), stack.end(), 0);
    return 0;
}
