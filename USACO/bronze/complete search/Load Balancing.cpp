/**
 * http://www.usaco.org/index.php?page=viewproblem2&cpid=617
 * Time: O(N^3)
 * Space: O(N)
 */

#include <bits/stdc++.h>

typedef long long ll;

using namespace std;

const int MAX_N = 100;
int x[MAX_N], y[MAX_N];

int main() {

    ios::sync_with_stdio(false);
    cin.tie(0);

    freopen("balancing.in", "r", stdin);
    freopen("balancing.out", "w", stdout);

    int n, b;
    cin >> n >> b;

    for (int i = 0; i < n; ++i)
        cin >> x[i] >> y[i];

    int res = n;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {

            int a = x[i], b = y[j];
            int quadrant[] = {0, 0, 0, 0};

            for (int k = 0; k < n; ++k) {
                if (x[k] <= a && y[k] <= b)
                    quadrant[0]++;
                else if (x[k] <= a && y[k] > b)
                    quadrant[1]++;
                else if (x[k] > a && y[k] > b)
                    quadrant[2]++;
                else
                    quadrant[3]++;
            }

            res = min(res, *max_element(quadrant, quadrant + 4));
        }
    }

    cout << res;
}