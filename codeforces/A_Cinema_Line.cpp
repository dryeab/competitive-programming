/**
 * https://codeforces.com/contest/349/problem/A
 * Time: O(n)
 * Space: O(1)
 */

#include <bits/stdc++.h>

using namespace std;

int main() {

    ios::sync_with_stdio(false);
    cin.tie(0);

    int n, x;
    cin >> n;

    int cng[] = {0, 0}; // 25, 50

    for (int i = n; i; --i) {

        cin >> x;

        if (x == 25) {
            cng[0]++;
        } else if (x == 50) {
            if (!cng[0]) {
                cout << "NO";
                return 0;
            } else {
                cng[0]--;
                cng[1]++;
            }
        } else {
            if ((cng[1] && cng[0])) {
                cng[0]--;
                cng[1]--;
            } else if (cng[0] >= 3) {
                cng[0] -= 3;
            } else {
                cout << "NO";
                return 0;
            }
        }
    }

    cout << "YES";
}