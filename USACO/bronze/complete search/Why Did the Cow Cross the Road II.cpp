/**
 * http://www.usaco.org/index.php?page=viewproblem2&cpid=712
 * Time: O(N^2)
 * Space: O(N)
 */

#include <bits/stdc++.h>

typedef long long ll;

using namespace std;

int main() {

    ios::sync_with_stdio(false);
    cin.tie(0);

    freopen("circlecross.in", "r", stdin);
    freopen("circlecross.out", "w", stdout);

    string s;
    cin >> s;

    int n = 52, res = 0;
    vector<int> start(26), end(26);

    for (int i = 1; i <= n; ++i) {
        char c = s[i - 1];
        if (start[c - 'A'])
            end[c - 'A'] = i;
        else
            start[c - 'A'] = i;
    }

    for (int i = 0; i < 26; ++i) {
        for (int j = i + 1; j < 26; ++j) {
            if ((start[i] < start[j] && start[j] < end[i] && end[i] < end[j]) || (start[i] > start[j] && start[i] < end[j] && end[i] > end[j])) {
                res++;
            }
        }
    }

    cout << res;
}