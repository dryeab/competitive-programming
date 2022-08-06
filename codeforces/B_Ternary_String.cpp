/**
 * https://codeforces.com/problemset/problem/1354/B
 * Time: O(N)
 * Space: O(N)
 */

#include <bits/stdc++.h>

typedef long long ll;

using namespace std;

int main() {

    ios::sync_with_stdio(false);
    cin.tie(0);

    int t;
    cin >> t;

    while (t--) {

        string s;
        cin >> s;

        int i = 0, j = 0, res = INT_MAX;
        int cnt[] = {0, 0, 0};

        while (j < s.size()) {
            cnt[s[j++] - '1']++;
            while (cnt[0] && cnt[2] && cnt[1]) {
                res = min(res, j - i);
                cnt[s[i++] - '1']--;
            }
        }

        cout << (res == INT_MAX ? 0 : res) << '\n';
    }
}

/*

int main() {

    ios::sync_with_stdio(false);
    cin.tie(0);

    int t;
    cin >> t;

    while (t--) {

        string s;
        cin >> s;

        int idx[] = {(int)-1e9, (int)-1e9, (int)-1e9}, res = INT_MAX;

        for (int i = 0; i < s.size(); ++i) {
            idx[s[i] - '1'] = i;
            res = min(res, i - min({idx[0], idx[1], idx[2]}) + 1);
        }

        cout << (res > s.size() ? 0 : res) << '\n';
    }
}

*/