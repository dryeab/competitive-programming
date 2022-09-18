
/**
 * https://codeforces.com/problemset/problem/478/B
 * Time: O(1)
 * Space: O(1)
 */

#include <bits/stdc++.h>

typedef long long ll;

using namespace std;

int main(int argc, char *argv[]) {

    ios::sync_with_stdio(false);
    cin.tie(0);

    ll n, m;
    cin >> n >> m;

    ll kmx = (1 + (n - m)) * ((n - m));

    ll normal = n / m, spare = n % m;

    ll with_normal = m - spare;

    ll kmn = (with_normal * (normal * (normal - 1))) + (spare * normal * (normal + 1));

    cout << kmn / 2 << ' ' << kmx / 2;
}
