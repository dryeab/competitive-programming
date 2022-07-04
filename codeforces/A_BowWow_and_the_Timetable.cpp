/**
 * https://codeforces.com/problemset/problem/1204/A
 * Time:
 * Space:
 */

#include <bits/stdc++.h>

using namespace std;

int main() {
    string s;
    cin >> s;

    int ones = count(s.begin(), s.end(), '1'), n;
    for (int i = 0; i < s.size(); ++i) {
        if (s[i] == '1') {
            cout << ceil((s.size() - i - (ones > 1 ? 0 : 1)) / 2.0);
            return 0;
        }
    }

    cout << 0;
}