/**
 * https://codeforces.com/contest/1157/problem/C2
 * Time:
 * Space:
 */

#include <bits/stdc++.h>

using namespace std;

int main() {

    ios::sync_with_stdio(false);
    cin.tie(0);

    int n;
    cin >> n;

    vector<int> a(n);
    for (int &x : a)
        cin >> x;

    int i = 0, j = n - 1, last = -1;
    vector<char> dxn;

    while (i <= j) {
        if (a[i] <= last && a[j] <= last)
            break;

        if (a[i] < a[j] && last < a[i]) {
            dxn.push_back('L');
            last = a[i];
            i++;
        } else if (a[j] < a[i] && last < a[j]) {
            dxn.push_back('R');
            last = a[j];
            j--;
        } else {
            int left = 0, right = 0;
            for (int k = i, l = last; k <= j; ++k) {
                if (l >= a[k])
                    break;
                left++, l = a[k];
            }
            for (int k = j, l = last; k >= i; --k) {
                if (l >= a[k])
                    break;
                right++, l = a[k];
            }

            if (left >= right)
                while (left--)
                    dxn.push_back('L');
            else
                while (right--) {
                    dxn.push_back('R');
                }

            break;
        }
    }

    cout << dxn.size() << '\n';
    for (auto x : dxn)
        cout << x;
}