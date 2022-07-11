/**
 * https://codeforces.com/contest/919/problem/B
 * Time:
 * Space: O(1)
 */

#include <bits/stdc++.h>

typedef long long ll;

using namespace std;

int sum(int i) {
    int res = 0;
    while (i) {
        res += i % 10;
        i /= 10;
    }
    return res;
}

int main() {

    ios::sync_with_stdio(false);
    cin.tie(0);

    int k;
    cin >> k;

    for (int i = 19;; ++i) {
        if (sum(i) == 10) {
            k--;
            if (k == 0) {
                cout << i;
                return 0;
            }
        }
    }
}