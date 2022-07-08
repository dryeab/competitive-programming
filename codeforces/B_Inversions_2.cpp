/**
 * https://codeforces.com/edu/course/2/lesson/4/3/practice/contest/274545/problem/B
 * Time:
 * Space:
 */

#include <bits/stdc++.h>

using ll = long long;

using namespace std;

struct segment_tree {

    int n;
    vector<int> tree;

    void init(int i) {

        n = 1;
        while (n < i)
            n <<= 1;

        tree.resize(2 * n);

        for (int j = n + i - 1; j > 0; --j) {
            if (j >= n)
                tree[j] = 1;
            else
                tree[j] = tree[2 * j] + tree[2 * j + 1];
        }
    }

    void set(int i) {

        i += n - 1;
        tree[i] = 0;

        for (i /= 2; i > 0; i /= 2) {
            tree[i] = tree[2 * i] + tree[2 * i + 1];
        }
    }

    int get(int i) {

        int root = 1;

        while (root < n) {
            if (tree[2 * root + 1] <= i) {
                i -= tree[2 * root + 1];
                root *= 2;
            } else {
                root = 2 * root + 1;
            }
        }

        return root - n + 1;
    }
};

int main() {

    ios::sync_with_stdio(false);
    cin.tie(0);

    int n, v;
    cin >> n;

    segment_tree st;
    st.init(n);

    vector<int> p(n);
    for (auto &x : p)
        cin >> x;

    vector<int> res;
    for (int i = n - 1; i >= 0; --i) {
        v = st.get(p[i]);
        res.push_back(v);
        st.set(v);
    }

    for (int i = n - 1; i >= 0; --i)
        cout << res[i] << ' ';
}