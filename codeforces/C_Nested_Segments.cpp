/**
 * https://codeforces.com/edu/course/2/lesson/4/3/practice/contest/274545/problem/C
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
    }

    void set(int i) {

        i += n;
        tree[i] = 1;

        for (i /= 2; i > 0; i /= 2) {
            tree[i] = tree[2 * i] + tree[2 * i + 1];
        }
    }

    int get(int l, int r) {
        l += n, r += n;
        int res = 0;
        while (l <= r) {
            if (l & 1)
                res += tree[l++];
            if (!(r & 1))
                res += tree[r--];
            l /= 2, r /= 2;
        }
        return res;
    }
};

int main() {

    ios::sync_with_stdio(false);
    cin.tie(0);

    int n;
    cin >> n;

    n *= 2;

    segment_tree st;
    st.init(n);

    vector<int> p(n);
    for (auto &x : p)
        cin >> x;

    vector<int> res(n / 2), left(n / 2 + 1, -1);

    for (int i = 0; i < n; ++i) {
        if (left[p[i]] != -1) {
            res[p[i] - 1] = st.get(left[p[i]] + 1, i - 1);
            st.set(left[p[i]]);
        } else {
            left[p[i]] = i;
        }
    }

    for (int x : res)
        cout << x << ' ';
}