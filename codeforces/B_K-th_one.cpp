/**
 * https://codeforces.com/edu/course/2/lesson/4/2/practice/contest/273278/problem/B
 * Time:
 * Space:
 */

#include <bits/stdc++.h>

using namespace std;

struct segment_tree {

    int n;
    vector<int> tree;

    void init(vector<int> &a) {

        n = 1;
        while (n < a.size())
            n *= 2;

        a.resize(n);
        tree.resize(2 * n);

        for (int i = 2 * n - 1; i > 0; --i) {
            if (i >= n) {
                tree[i] = a[i - n];
            } else {
                tree[i] = tree[2 * i] + tree[2 * i + 1];
            }
        }
    }

    void set(int i) {

        i += n;
        tree[i] = (tree[i] + 1) % 2;

        for (i /= 2; i > 0; i /= 2) {
            tree[i] = tree[2 * i] + tree[2 * i + 1];
        }
    }

    int findKth(int k) {

        int root = 1;

        while (root < n) {
            if (tree[2 * root] >= k)
                root = 2 * root;
            else {
                k -= tree[2 * root];
                root = 2 * root + 1;
            }
        }

        return root - n;
    }
};

int main() {

    ios::sync_with_stdio(false);
    cin.tie(0);

    int n, m;
    cin >> n >> m;

    vector<int> a(n);
    for (int &x : a)
        cin >> x;

    segment_tree st;
    st.init(a);

    int op, v;
    for (int i = 0; i < m; ++i) {
        cin >> op >> v;
        if (op == 1) {
            st.set(v);
        } else {
            cout << st.findKth(v + 1) << endl;
        }
    }
}