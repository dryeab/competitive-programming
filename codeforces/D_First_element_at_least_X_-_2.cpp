/**
 * https://codeforces.com/edu/course/2/lesson/4/2/practice/contest/273278/problem/D
 * Time:
 * Space:
 */

// doesn't pass

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

    int minJ(int x, int l, int root, int lr, int rr) {

        if (tree[root] < x)
            return -1;

        if (root >= n)
            return root - n;

        int res = -1, mr = (lr + rr) / 2;

        if (mr >= l && tree[2 * root] >= x) {
            res = minJ(x, l, 2 * root, lr, mr);
            if (res != -1)
                return res;
        }

        res = minJ(x, l, 2 * root + 1, mr + 1, rr);

        return res;

        // int root = 1, lr = 0, rr = n - 1, mr;

        // while (1) {

        //     if (tree[root] < x)
        //         return -1;

        //     if (root >= n)
        //         return root - n;

        //     mr = (lr + rr) / 2;

        //     if (tree[2 * root] >= x && mr >= l) {
        //         root = 2 * root;
        //         rr = mr;
        //     } else {
        //         root = 2 * root + 1;
        //         lr = mr + 1;
        //     }
        // }

        // return (tree[root] >= x ? root - n : -1);
        // return -1;
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

    int op, y, z;
    while (m--) {
        cin >> op >> y >> z;
        if (op == 1) {
            st.set(y, z);
        } else {
            cout << st.minJ(y, z, 1, 0, st.n - 1) << endl;
        }
    }
}