#include <iostream>
#include <set>
#include <string>

using namespace std;

int N;
multiset<string> participants;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    cin >> N;
    for (int i = 0; i < N; i++) {
        string name;
        cin >> name;
        participants.insert(name);
    }
    for (int i = 0; i < N - 1; i++) {
        string name;
        cin >> name;
        participants.erase(participants.find(name));
    }
    cout << *participants.begin();
    return 0;
}
