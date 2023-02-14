#include <iostream>
#include <string>

using namespace std;
string s;
int result;

int main() {
    cin >> s;
    for (int i = 0; i < s.length(); i++)
        result = (result * 10 + (s.at(i) - '0')) % 20000303;
    cout << result;

    return 0;
}