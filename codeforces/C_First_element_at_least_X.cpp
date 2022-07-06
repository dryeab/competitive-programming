/**
 * https://codeforces.com/edu/course/2/lesson/4/2/practice/contest/273278/problem/C
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

        a.resize(n, -1);
        tree.resize(2 * n);

        for (int i = 2 * n - 1; i > 0; i--) {
            if (i >= n) {
                tree[i] = a[i - n];
            } else
                tree[i] = max(tree[2 * i], tree[2 * i + 1]);
        }
    }

    void set(int i, int v) {

        i += n;
        tree[i] = v;

        for (i /= 2; i > 0; i /= 2) {
            tree[i] = max(tree[2 * i], tree[2 * i + 1]);
        }
    }

    int minJ(int x) {

        if (tree[1] < x)
            return -1;

        int root = 1;

        while (root < n) {
            if (tree[2 * root] >= x)
                root = 2 * root;
            else
                root = 2 * root + 1;
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
    for (int &i : a)
        cin >> i;

    segment_tree st;
    st.init(a);

    int op, i, v, x;
    while (m--) {
        cin >> op;
        if (op == 1) {
            cin >> i >> v;
            st.set(i, v);
        } else {
            cin >> x;
            cout << st.minJ(x) << endl;
        }
    }
}