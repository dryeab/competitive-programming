/**
 * https://codeforces.com/contest/186/problem/A
 * Time: O(n)
 * Space: O(n)
 */

#include <bits/stdc++.h>

using namespace std;

int main() {

    ios::sync_with_stdio(false);
    cin.tie(0);

    string first, second;
    cin >> first >> second;

    if (first.size() != second.size()) {
        cout << "NO";
        return 0;
    }

    int n = first.size(), cnt = 0, l = -1;
    for (int i = 0; i < n; ++i) {
        cnt += first[i] != second[i];
    }

    if (cnt != 2) {
        cout << "NO";
        return 0;
    }

    for (int i = 0; i < n; ++i) {
        if (first[i] != second[i]) {
            if (l == -1) {
                l = i;
            } else {
                if (first[i] == second[l] && first[l] == second[i]) {
                    cout << "YES";
                } else {
                    cout << "NO";
                }
                return 0;
            }
        }
    }
    cout << "NO";
}