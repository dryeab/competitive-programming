/**
 * http://www.usaco.org/index.php?page=viewproblem2&cpid=1013
 * Time: O(N^2)
 * Space: O(N)
 */

#include <bits/stdc++.h>

using namespace std;

int main() {

    ios::sync_with_stdio(false);
    cin.tie(0);

    freopen("swap.in", "r", stdin);
    freopen("swap.out", "w", stdout);

    int n, k;
    cin >> n >> k;

    int a1, a2, b1, b2;
    cin >> a1 >> a2 >> b1 >> b2;
    a1--, a2--, b1--, b2--;

    vector<int> end(n), change(n);

    for (int i = 0; i < n; ++i)
        end[i] = i;

    for (int i = a1, j = a2; i < j; ++i, j--)
        swap(end[i], end[j]);

    for (int i = b1, j = b2; i < j; ++i, j--)
        swap(end[i], end[j]);

    for (int i = 0; i < n; ++i)
        change[end[i]] = i;

    vector<int> res(n);

    for (int i = 0; i < n; ++i) {

        int pos = i;
        vector<int> visited(n, -1);

        for (int j = 0; j < k; ++j) {

            if (visited[pos] != -1) {

                int cycle = j - visited[pos], tempK = k;
                tempK = (tempK - j) % cycle;

                while (tempK--)
                    pos = change[pos];

                break;
            }

            visited[pos] = j;
            pos = change[pos];
        }

        res[pos] = i;
    }

    for (int x : res)
        cout << (x + 1) << '\n';
}