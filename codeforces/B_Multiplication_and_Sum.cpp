/**
 * https://codeforces.com/edu/course/2/lesson/5/2/practice/contest/279653/problem/B
 * Time:
 * Space:
 */

#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

const ll MOD = 1e9 + 7;

struct segment_tree {

    ll n;
    vector<ll> ops, sum;

    ll add_op(ll a, ll b) {
        return (a + b) % MOD;
    }

    ll mul_op(ll a, ll b) {
        return (a * b) % MOD;
    }

    segment_tree(ll j) {

        n = (1ll << int(ceil(log2(j))));
        ops.resize(2 * n, 1ll);
        sum.resize(2 * n, 1ll);

        for (int i = n - 1; i > 0; --i)
            sum[i] = add_op(sum[2 * i], sum[2 * i + 1]);
    }

    void multiply(ll v, ll l, ll r, ll root, ll rl, ll rr) {

        if (rl > r || rr < l)
            return;

        if (l <= rl && r >= rr) {
            ops[root] = mul_op(ops[root], v);
            sum[root] = mul_op(sum[root], v);
            return;
        }

        ll m = rl + (rr - rl) / 2;
        multiply(v, l, r, 2 * root, rl, m);
        multiply(v, l, r, 2 * root + 1, m + 1, rr);

        sum[root] = mul_op(add_op(sum[2 * root], sum[2 * root + 1]), ops[root]);
    }

    void multiply(ll l, ll r, ll v) {
        multiply(v, l, r, 1, 0, n - 1);
    }

    ll getSum(ll l, ll r, ll root, ll rl, ll rr) {

        if (rl > r || rr < l)
            return 0;

        if (l <= rl && r >= rr) {
            return sum[root];
        }

        ll m = rl + (rr - rl) / 2;

        return mul_op(add_op(getSum(l, r, 2 * root, rl, m), getSum(l, r, 2 * root + 1, m + 1, rr)), ops[root]);
    }

    ll getSum(ll l, ll r) {
        return getSum(l, r, 1, 0, n - 1);
    }
};

int main() {

    ios::sync_with_stdio(false);
    cin.tie(0);

    ll n, m, op, l, r, v, i;
    cin >> n >> m;

    segment_tree st(n);

    for (ll j = 0; j < m; ++j) {
        cin >> op;
        if (op == 1) {
            cin >> l >> r >> v;
            st.multiply(l, r - 1, v);
        } else {
            cin >> l >> r;
            cout << st.getSum(l, r - 1) << "\n";
        }
    }
}