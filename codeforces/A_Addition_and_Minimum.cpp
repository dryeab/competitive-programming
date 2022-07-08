/**
 * https://codeforces.com/edu/course/2/lesson/5/2/practice/contest/279653/problem/A
 * Time:
 * Space:
 */

#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

struct segment_tree {

    int n;
    vector<ll> ops, mins;

    segment_tree(int i) {
        n = (1 << int(ceil(log2(i))));
        ops.resize(2 * n, 0);
        mins.resize(2 * n, 0);
    }

    void add(int v, int l, int r, int root, int rl, int rr) {

        if (rl > r || rr < l)
            return;

        if (l <= rl && r >= rr) {
            ops[root] += v;
            mins[root] += v;
            return;
        }

        int m = rl + (rr - rl) / 2;
        add(v, l, r, 2 * root, rl, m);
        add(v, l, r, 2 * root + 1, m + 1, rr);

        mins[root] = min(mins[2 * root], mins[2 * root + 1]) + ops[root];
    }

    void add(int l, int r, int v) {
        add(v, l, r, 1, 0, n - 1);
    }

    ll getMin(int l, int r, int root, int rl, int rr) {
        if (rl > r || rr < l)
            return LLONG_MAX;
        if (l <= rl && r >= rr) {
            return mins[root];
        }
        int m = rl + (rr - rl) / 2;
        return min(getMin(l, r, 2 * root, rl, m), getMin(l, r, 2 * root + 1, m + 1, rr)) + ops[root];
    }

    ll getMin(int l, int r) {
        return getMin(l, r, 1, 0, n - 1);
    }
};

int main() {

    ios::sync_with_stdio(false);
    cin.tie(0);

    int n, m, op, l, r, v, i;
    cin >> n >> m;

    segment_tree st(n);

    for (int j = 0; j < m; ++j) {
        cin >> op;
        if (op == 1) {
            cin >> l >> r >> v;
            st.add(l, r - 1, v);
        } else {
            cin >> l >> r;
            cout << st.getMin(l, r - 1) << "\n";
        }
    }
}