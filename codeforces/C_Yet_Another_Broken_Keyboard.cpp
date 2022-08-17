/**
 * https://codeforces.com/problemset/problem/1272/C
 * Time: O(N)
 * Space: O(N)
 */
 
 #include <bits/stdc++.h>

typedef long long ll;

using namespace std;

int main() {

    ios::sync_with_stdio(false);
    cin.tie(0);

    int n, k;
    string s;

    cin >> n >> k >> s;

    ll res = 0, cnt = 0;
    vector<bool> exists(26);

    for (int i = 0; i < k; ++i) {
        char c;
        cin >> c;
        exists[c - 'a'] = true;
    }

    for (char c : s) {
        if (exists[c - 'a'])
            cnt++;
        else
            cnt = 0;
        res += cnt;
    }

    cout << res;
}