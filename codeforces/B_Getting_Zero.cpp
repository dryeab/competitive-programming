/**
 * https://codeforces.com/problemset/problem/1661/B
 * Time: O(N)
 * Space: O(1)
 */

#include <bits/stdc++.h>

typedef long long ll;

using namespace std;

int main() {

    ios::sync_with_stdio(false);
    cin.tie(0);

    int n, k = 1 << 15;
    cin >> n;

    for (int i = 0; i < n; ++i) {

        int a, ans = 1e9;
        cin >> a;

        for (int sum = 0; sum < 16; sum++) {
            for (int mul = 0; mul < 16; mul++)
                if (((a + sum) << mul) % k == 0)
                    ans = min(ans, sum + mul);
        }

        cout << ans << ' ';
    }
}