#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct segment_tree
{
    int n;
    vector<int> tree;

    void init(vector<int> &arr)
    {
        n = 1;
        while (n < arr.size())
            n *= 2;

        arr.resize(n, 1e9 + 1);
        tree.resize(2 * n, 0);

        for (int i = 2 * n - 1; i >= 1; --i)
        {
            if (i >= n)
                tree[i] = arr[i - n];
            else
                tree[i] = min(tree[2 * i], tree[2 * i + 1]);
        }
    }

    int minimum(int l, int r)
    {
        l += n;
        r += n;

        int res = 1e9 + 1;

        while (l <= r)
        {
            if (l % 2 == 1)
                res = min(res, tree[l++]);

            if (r % 2 == 0)
                res = min(res, tree[r--]);

            l /= 2;
            r /= 2;
        }

        return res;
    }

    void set(int i, int v)
    {
        i += n;
        tree[i] = v;

        for (i /= 2; i >= 1; i /= 2)
            tree[i] = min(tree[2 * i], tree[2 * i + 1]);
    }
};

int main()
{

    ios::sync_with_stdio(false);
    cin.tie(0);
    
    int n, m;
    cin >> n >> m;

    vector<int> arr(n);
    for (auto &x : arr)
        cin >> x;

    segment_tree st;
    st.init(arr);

    while (m--)
    {
        int op, a, b;
        cin >> op >> a >> b;

        if (op == 1)
            st.set(a, b);
        else
            cout << st.minimum(a, b - 1) << endl;
    }
}