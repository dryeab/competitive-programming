/**
 * https://codeforces.com/contest/1157/problem/A
 * Time:
 * Space:
 */

#include <bits/stdc++.h>

typedef long long ll;

using namespace std;

int main() {

    ios::sync_with_stdio(false);
    cin.tie(0);

    int n;
    cin >> n;

    set<int> seen;
    while (!seen.count(n)) {
        seen.insert(n);
        n++;
        while (!(n % 10))
            n /= 10;
    }
    cout << res;
}