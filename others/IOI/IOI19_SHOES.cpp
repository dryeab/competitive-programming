#include <bits/stdc++.h>

using namespace std;

struct segment_tree {

    int n;
    vector<int> tree;

    void init(int i) {
        n = 1;
        while (n < i)
            n *= 2;
        tree.resize(2 * n, 0);
    }

    void set(int i) {
        i += n;
        tree[i] = 1;
        for (i /= 2; i > 0; i /= 2)
            tree[i] = tree[2 * i] + tree[2 * i + 1];
    }

    int get(int l, int r) {
        l += n;
        r += n;
        int res = 0;
        while (l <= r) {
            if (l & 1)
                res += tree[l++];
            if (!(r & 1))
                res += tree[r--];
            r /= 2, l /= 2;
        }
        return res;
    }
};

long long count_swaps(vector<int> s) {

    int n = s.size(), shift = 0;

    vector<vector<int>> left(n / 2 + 1), right(n / 2 + 1);
    for (int i = n - 1; i >= 0; --i) {
        if (s[i] < 0)
            left[-s[i]].push_back(i);
        else
            right[s[i]].push_back(i);
    }

    long long res = 0;

    segment_tree st;
    st.init(n);

    for (int i = 0, j; i < n; ++i) {

        if (s[i] == 0) {
            continue;
        } else if (s[i] > 0) {

            j = left[s[i]][left[s[i]].size() - 1];
            left[s[i]].pop_back();
            right[s[i]].pop_back();

            shift = st.get(i + 1, j - 1);
            res += j - i - shift;
            s[j] = s[i] = 0;

            st.set(i), st.set(j);
        } else {

            j = right[-s[i]][right[-s[i]].size() - 1];
            right[-s[i]].pop_back();
            left[-s[i]].pop_back();

            shift = st.get(i + 1, j - 1);

            res += j - i - shift - 1;

            s[j] = s[i] = 0;
            st.set(i), st.set(j);
        }
    }

    return res;
}