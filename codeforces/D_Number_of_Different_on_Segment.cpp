/**
 * https://codeforces.com/edu/course/2/lesson/4/4/practice/contest/274684/problem/D
 * Time:
 * Space:
 */

#include <bits/stdc++.h>

using ll = long long;

using namespace std;

struct segment_tree {

    int n;
    vector<ll> tree;

    void init(vector<int> &a) {

        n = 1;
        while (n < a.size())
            n *= 2;

        a.resize(n);
        tree.resize(2 * n);

        for (int i = 2 * n - 1; i > 0; --i) {
            if (i >= n) {
                tree[i] = (1ll << a[i - n]);
            } else {
                tree[i] = tree[2 * i] | tree[2 * i + 1];
            }
        }
    }

    void set(int i, int v) {

        i += n;
        tree[i] = (1ll << v);

        for (i /= 2; i > 0; i /= 2) {
            tree[i] = tree[2 * i] | tree[2 * i + 1];
        }
    }

    int get(int l, int r) {

        l += n, r += n;
        ll res = 0;

        while (l <= r) {
            if (l & 1) {
                res |= tree[l++];
            }
            if (!(r & 1)) {
                res |= tree[r--];
            }
            l >>= 1, r >>= 1;
        }
        return __builtin_popcountll(res);
    }
};

int main() {

    ios::sync_with_stdio(false);
    cin.tie(0);

    int n, q;
    cin >> n >> q;

    vector<int> a(n);
    for (int &x : a)
        cin >> x;

    segment_tree st;
    st.init(a);

    int type, x, y;
    for (int i = 0; i < q; ++i) {
        cin >> type >> x >> y;
        if (type == 1) {
            cout << st.get(x - 1, y - 1) << "\n";
        } else {
            st.set(x - 1, y);
        }
    }
}