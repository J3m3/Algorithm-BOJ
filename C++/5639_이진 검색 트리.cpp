#include <iostream>
#include <vector>

using namespace std;

vector<int> tree;
int n, root, left, right;

void post_order(int s, int e) {
    if (s >= e)
        return;

    int bound = e;
    for (int i = s + 1; i < e; i++)
        if (tree[s] < tree[i]) {
            bound = i;
            break;
        }
    post_order(s + 1, bound);
    post_order(bound, e);

    cout << tree[s] << '\n';
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    while (cin >> n)
        tree.push_back(n);

    post_order(0, tree.size());
    return 0;
}
