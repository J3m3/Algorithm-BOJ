#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

vector<string> pearl_in_night_sky(int n) {
    if (n == 1) {
        vector<string> unit = {"*"};
        return unit;
    }

    vector<string> stars = pearl_in_night_sky(n / 3);
    vector<string> result;

    auto it = stars.begin();
    for (; it != stars.end(); ++it) {
        string temp = "";
        for (int i = 0; i < 3; i++)
            temp += *it;
        result.push_back(temp);
    }

    it = stars.begin();
    for (; it != stars.end(); ++it) {
        string temp = *it;
        for (int i = 0; i < n / 3; i++)
            temp += " ";
        temp += *it;
        result.push_back(temp);
    }

    it = stars.begin();
    for (; it != stars.end(); ++it) {
        string temp = "";
        for (int i = 0; i < 3; i++)
            temp += *it;
        result.push_back(temp);
    }

    return result;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    int n;
    cin >> n;
    vector<string> result = pearl_in_night_sky(n);

    auto it = result.begin();
    for (; it != result.end(); ++it)
        cout << *it << '\n';

    return 0;
}