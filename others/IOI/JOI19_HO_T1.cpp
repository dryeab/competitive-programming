#include <bits/stdc++.h>

using namespace std;

int main() {

    ios::sync_with_stdio(false);
    cin.tie(0);

    int h, w;
    cin >> h >> w;

    vector<vector<char>> grid(h, vector<char>(w));
    vector<int> countO(h), countI(w);

    for (int i = 0; i < h; ++i) {
        for (int j = 0; j < w; ++j)
            cin >> grid[i][j];
    }

    long long res = 0;
    for (int i = h - 1; i >= 0; --i) {
        for (int j = w - 1; j >= 0; --j) {
            countO[i] += grid[i][j] == 'O';
            countI[j] += grid[i][j] == 'I';
            if (grid[i][j] == 'J')
                res += countI[j] * countO[i];
        }
    }

    cout << res;
}