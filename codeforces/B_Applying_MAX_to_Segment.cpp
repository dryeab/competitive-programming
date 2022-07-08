/**
 * https://codeforces.com/edu/course/2/lesson/5/1/practice/contest/279634/problem/B
 * Time:
 * Space:
 */

#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

struct segment_tree {

    int n;
    vector<int> tree;

    segment_tree(int i) {
        n = (1 << int(ceil(log2(i))));
        tree.resize(2 * n);
    }

    void maximum(int v, int l, int r, int root, int rl, int rr) {
        if (rl > r || rr < l)
            return;
        else if (l <= rl && r >= rr) {
            tree[root] = max(tree[root], v);
            return;
        }
        int m = rl + (rr - rl) / 2;
        maximum(v, l, r, 2 * root, rl, m);
        maximum(v, l, r, 2 * root + 1, m + 1, rr);
    }

    void maximum(int l, int r, int v) {
        maximum(v, l, r, 1, 0, n - 1);
    }

    int get(int i) {
        int res = 0;
        i += n;
        for (; i > 0; i /= 2)
            res = max(res, tree[i]);
        return res;
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
            st.maximum(l, r - 1, v);
        } else {
            cin >> i;
            cout << st.get(i) << "\n";
        }
    }
}