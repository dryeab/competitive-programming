/**
 * https://codeforces.com/contest/287/problem/A
 * Time: O(1)
 * Space: O(1)
 */

#include <bits/stdc++.h>

typedef long long ll;

using namespace std;

int main() {

    ios::sync_with_stdio(false);
    cin.tie(0);

    char grid[4][4];
    for (int i = 0; i < 4; ++i) {
        for (int j = 0; j < 4; ++j) {
            cin >> grid[i][j];
            if (j & i) {
                int cnt = 0;
                cnt += grid[i][j] == '.';
                cnt += grid[i - 1][j] == '.';
                cnt += grid[i][j - 1] == '.';
                cnt += grid[i - 1][j - 1] == '.';
                if (cnt != 2) {
                    cout << "YES";
                    return 0;
                }
            }
        }
    }

    cout << "NO";
}