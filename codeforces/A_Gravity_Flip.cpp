/**
 * https://codeforces.com/problemset/problem/405/A
 * Time: O(NlogN)
 * Space: O(N)
 */

#include <bits/stdc++.h>

typedef long long ll;

using namespace std;

int main() {

    ios::sync_with_stdio(false);
    cin.tie(0);

    int n;
    cin >> n;

    vector<int> a(n);
    for (int &i : a)
        cin >> i;

    sort(a.begin(), a.end());

    for (int i : a)
        cout << i << ' ';
}