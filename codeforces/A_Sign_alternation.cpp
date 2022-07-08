/**
 * https://codeforces.com/edu/course/2/lesson/4/4/practice/contest/274684/problem/A
 * Time:
 * Space:
 */

#include <bits/stdc++.h>

using ll = long long;

using namespace std;

struct segment_tree {

    int n;
    vector<pair<int, int>> tree;

    void init(vector<int> &a) {

        n = 1;
        while (n < a.size())
            n <<= 1;

        a.resize(n);
        tree.resize(2 * n);

        for (int i = 2 * n - 1; i > 0; --i) {
            if (i >= n) {
                if (i & 1) {
                    tree[i] = {0, a[i - n]};
                } else {
                    tree[i] = {a[i - n], 0};
                }
            } else {
                tree[i].first = tree[2 * i].first + tree[2 * i + 1].first;
                tree[i].second = tree[2 * i].second + tree[2 * i + 1].second;
            }
        }
    }

    void set(int i, int v) {

        i += n;

        if (i & 1) {
            tree[i] = {0, v};
        } else {
            tree[i] = {v, 0};
        }

        for (i /= 2; i > 0; i /= 2) {
            tree[i].first = tree[2 * i].first + tree[2 * i + 1].first;
            tree[i].second = tree[2 * i].second + tree[2 * i + 1].second;
        }
    }

    pair<int, int> get(int l, int r) {
        pair<int, int> res = {0, 0};
        l += n, r += n;
        while (l <= r) {
            if (l & 1) {
                res.first += tree[l].first;
                res.second += tree[l].second;
                l++;
            }
            if (!(r & 1)) {
                res.first += tree[r].first;
                res.second += tree[r].second;
                r--;
            }
            l /= 2, r /= 2;
        }
        return res;
    }
};

int main() {

    ios::sync_with_stdio(false);
    cin.tie(0);

    int n, m;
    cin >> n;

    vector<int> a(n);
    for (int &x : a)
        cin >> x;

    segment_tree st;
    st.init(a);

    cin >> m;
    int op, i, j, l, r;

    while (m--) {
        cin >> op;
        if (op == 0) {
            cin >> i >> j;
            st.set(i - 1, j);
        } else {
            cin >> l >> r;
            l--, r--;
            pair<int, int> res = st.get(l, r);
            if (l & 1) {
                cout << res.second - res.first << '\n';
            } else {
                cout << res.first - res.second << '\n';
            }
        }
    }
}