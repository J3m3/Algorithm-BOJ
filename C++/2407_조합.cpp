#include <algorithm>
#include <iostream>
#include <string>

using namespace std;

int n, m;
string dp[101][101];

string add_string(const string &a, const string &b) {
    string result = "";
    int sum = 0;
    int length = max(a.length(), b.length());

    for (int i = 0; i < length || sum; i++) {
        if (a.length() > i)
            sum += a[i] - '0';
        if (b.length() > i)
            sum += b[i] - '0';

        result += (sum % 10) + '0';
        sum /= 10;
    }

    return result;
}

string combination(int n, int m) {
    if (n == m || m == 0)
        return "1";

    if (dp[n][m] != "")
        return dp[n][m];

    dp[n][m] = add_string(combination(n - 1, m - 1), combination(n - 1, m));
    return dp[n][m];
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    cin >> n >> m;

    string result = combination(n, m);
    reverse(result.begin(), result.end());
    cout << result;

    return 0;
}