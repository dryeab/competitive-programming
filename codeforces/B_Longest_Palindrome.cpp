/**
 * https://codeforces.com/problemset/problem/1304/B
 * Time: O(NMlogN)
 * Space: O(N)
 */

#include <bits/stdc++.h>

typedef long long ll;

using namespace std;

int main() {

    ios::sync_with_stdio(false);
    cin.tie(0);

    int n, m;
    cin >> n >> m;

    string ans, mid;
    set<string> strs;

    for (int i = 0; i < n; ++i) {

        string s;
        cin >> s;

        strs.insert(s);

        string t = s;
        reverse(t.begin(), t.end());

        if (strs.count(t))
            if (s == t)
                mid = t;
            else
                ans += s;
    }

    string t = ans;
    reverse(t.begin(), t.end());

    ans += mid + t;

    cout << ans.size() << "\n";
    cout << ans;
}