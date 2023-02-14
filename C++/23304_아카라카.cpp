#include <iostream>
#include <string>

using namespace std;

#define fastio ios_base::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr)

bool is_palindrome(string &seq, int l, int r) {
    if (l >= r)
        return true;
    
    if (seq[l] != seq[r])
        return false;
    
    return is_palindrome(seq, l+1, r-1);
}

bool is_akaraka(string &seq, int l, int r) {
    if (l >= r)
        return true;
    
    if (!is_palindrome(seq, l, r))
        return false;
    
    int mid = (l + r) / 2;
    if ((l + r) & 1)
        return is_akaraka(seq, l, mid);
    else
        return is_akaraka(seq, l, mid-1);
}

int main() {
    fastio;
    string seq;
    cin >> seq;

    if (is_akaraka(seq, 0, seq.length()-1))
        cout << "AKARAKA";
    else
        cout << "IPSELENTI";
    
    return 0;
}