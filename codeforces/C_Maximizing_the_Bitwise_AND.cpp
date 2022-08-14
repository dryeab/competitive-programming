/**
 * https://codeforces.com/group/KIrM1Owd8u/contest/265924/problem/C
 * Time: O(N)
 * Space: O(N)
 */

#include <bits/stdc++.h>

typedef long long ll;

using namespace std;

vector<int> a;

vector<int> clear(int i) {
    vector<int> res;
    for (int x : a) {
        if ((x >> i) & 1)
            res.push_back(x);
    }
    return res;
}

int main() {

    ios::sync_with_stdio(false);
    cin.tie(0);

    int n;
    cin >> n;

    a.resize(n);
    for (int &i : a)
        cin >> i;

    int i = 31;
    while (i >= 0) {
        auto res = clear(i);
        if (res.size() > 1)
            a = res;
        i--;
    }

    cout << (a[0] & a[1]);
}