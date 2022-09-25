/**
 * http://www.usaco.org/index.php?page=viewproblem2&cpid=640
 * Time: O(K^2 * M^6)
 * Space: O(KM
 */

#include <bits/stdc++.h>

typedef long long ll;

using namespace std;

const int MAX_N = 8, MAX_K = 10;
char original[MAX_N][MAX_N], pieces[MAX_K][MAX_N][MAX_N];

int N, K;

bool inBound(int i, int j) {
    return 0 <= i && i < N && 0 <= j && j < N;
}

bool correct(int k1, int k2) {

    for (int a = -N; a <= N; ++a) {
        for (int b = -N; b <= N; ++b) {
            for (int c = -N; c <= N; ++c) {
                for (int d = -N; d <= N; ++d) {

                    bool ok = true;
                    vector<vector<char>> cur(N, vector<char>(N, '.'));

                    for (int i = 0; i < N && ok; ++i) {
                        for (int j = 0; j < N && ok; ++j) {
                            if (pieces[k1][i][j] == '#') {
                                int ni = i + a, nj = j + b;
                                if (inBound(ni, nj) && cur[ni][nj] == '.')
                                    cur[ni][nj] = '#';
                                else
                                    ok = false;
                            }
                        }
                    }

                    for (int i = 0; i < N && ok; ++i) {
                        for (int j = 0; j < N && ok; ++j) {
                            if (pieces[k2][i][j] == '#') {
                                int ni = i + c, nj = j + d;
                                if (inBound(ni, nj) && cur[ni][nj] == '.')
                                    cur[ni][nj] = '#';
                                else
                                    ok = false;
                            }
                        }
                    }

                    for (int i = 0; i < N && ok; ++i) {
                        for (int j = 0; j < N && ok; ++j) {
                            ok = ok && (cur[i][j] == original[i][j]);
                        }
                    }

                    if (ok)
                        return true;
                }
            }
        }
    }

    return false;
}

int main() {

    ios::sync_with_stdio(false);
    cin.tie(0);

    freopen("bcs.in", "r", stdin);
    freopen("bcs.out", "w", stdout);

    cin >> N >> K;

    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
            cin >> original[i][j];
        }
    }

    for (int i = 0; i < K; ++i) {
        for (int j = 0; j < N; ++j) {
            for (int k = 0; k < N; ++k) {
                cin >> pieces[i][j][k];
            }
        }
    }

    for (int i = 0; i < K; ++i) {
        for (int j = i + 1; j < K; ++j) {
            if (correct(i, j)) {
                cout << i + 1 << ' ' << j + 1;
                return 0;
            }
        }
    }
}