/**
 * https://codeforces.com/problemset/problem/706/B
 * Time: O(q * log(n))
 * Space: O(n)
 */

#include <bits/stdc++.h>

using namespace std;

int main() {

    ios::sync_with_stdio(false);
    cin.tie(0);

    int n, q;
    cin >> n;

    vector<int> x(n);
    for (int &i : x)
        cin >> i;

    sort(x.begin(), x.end());

    cin >> q;

    int m;
    while (q--) {

        cin >> m;

        // int l, r, mid, res;
        // l = 0, r = n;

        // while (l < r) {

        //     mid = (l + r) / 2;

        //     if (x[mid] <= m)
        //         l = mid + 1;
        //     else
        //         r = mid;
        // }

        // ;

        // lower_bound();

        cout << upper_bound(x.begin(), x.end(), m) - x.begin() << endl;
    }
}