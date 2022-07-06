/**
 * https://codeforces.com/edu/course/2/lesson/4/3/practice/contest/274545/problem/A
 * Time: O(n * log(n))
 * Space: O(n)
 */

#include <bits/stdc++.h>

using namespace std;

struct segment_tree {
    int n;
    vector<int> tree;

    void init(int size) {
        n = 1;
        while (n < size)
            n *= 2;
        tree.resize(2 * n, 0);
    }

    int set(int i) {

        i += n - 1;
        tree[i]++;

        int res = 0, l = i + 1, r = 2 * n - 1;

        for (int j = i / 2; j > 0; j /= 2) {
            tree[j] = tree[2 * j] + tree[2 * j + 1];
        }

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

    int n, x;
    cin >> n;

    segment_tree st;
    st.init(n);

    for (int i = 0; i < n; ++i) {
        cin >> x;
        cout << st.set(x) << " ";
    }
}