/**
 * https://codeforces.com/edu/course/2/lesson/4/3/practice/contest/274545/problem/E
 * Time:
 * Space:
 */

#include <bits/stdc++.h>

using ll = long long;

using namespace std;

struct segment_tree {

    int n;
    vector<ll> up, down;

    void init(int i) {

        n = 1;
        while (n < i)
            n <<= 1;

        up.resize(2 * n);
        down.resize(2 * n);
    }

    void set(ll i, ll v) {

        i += n;

        if (v >= 0) {
            up[i] += v;
            for (i /= 2; i > 0; i /= 2) {
                up[i] = up[2 * i] + up[2 * i + 1];
            }
        } else {
            down[i] += v;
            for (i /= 2; i > 0; i /= 2) {
                down[i] = down[2 * i] + down[2 * i + 1];
            }
        }
    }

    ll getUp(ll i) {

        int l = n, r = i + n;
        ll res = 0;

        while (l <= r) {
            if (l & 1)
                res += up[l++];
            if (!(r & 1))
                res += up[r--];
            l /= 2, r /= 2;
        }
        return res;
    }

    ll getDown(ll i) {

        int l = n, r = i + n;
        ll res = 0;

        while (l <= r) {
            if (l & 1)
                res += down[l++];
            if (!(r & 1))
                res += down[r--];
            l /= 2, r /= 2;
        }
        return res;
    }
};

int main() {

    ios::sync_with_stdio(false);
    cin.tie(0);

    int n, m;
    cin >> n >> m;

    segment_tree st;
    st.init(n);

    ll op, l, r, v, i;
    for (int j = 0; j < m; ++j) {
        cin >> op;
        if (op == 1) {
            cin >> l >> r >> v;
            st.set(l, v);      // up
            st.set(r - 1, -v); // down
        } else {
            cin >> i;
            cout << st.getUp(i) + st.getDown(i - 1) << "\n";
        }
    }
}