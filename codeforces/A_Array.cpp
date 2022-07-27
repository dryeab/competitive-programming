/**
 * https://codeforces.com/problemset/problem/300/A
 * Time: O(n)
 * Space: O(n)
 */

#include <bits/stdc++.h>

typedef long long ll;

using namespace std;

int main() {

    ios::sync_with_stdio(false);
    cin.tie(0);

    int n, x;
    cin >> n;

    vector<int> neg, zero, pos;
    for (int i = 0; i < n; ++i) {
        cin >> x;
        if (x == 0)
            zero.push_back(x);
        else if (x > 0)
            pos.push_back(x);
        else
            neg.push_back(x);
    }

    if (!(neg.size() & 1)) {
        zero.push_back(neg[neg.size() - 1]);
        neg.pop_back();
    }

    if (!(pos.size())) {
        int t = 2;
        while (t--) {
            pos.push_back(neg[neg.size() - 1]);
            neg.pop_back();
        }
    }

    cout << neg.size() << ' ';
    for (int x : neg)
        cout << x << ' ';
    cout << '\n';

    cout << pos.size() << ' ';
    for (int x : pos)
        cout << x << ' ';
    cout << '\n';

    cout << zero.size() << ' ';
    for (int x : zero)
        cout << x << ' ';
    cout << '\n';
}