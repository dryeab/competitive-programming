#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct segment_tree
{
    int n;
    vector<vector<long long>> tree;

    void init(vector<long long> &arr)
    {
        n = 1;
        while (n < arr.size())
            n *= 2;

        arr.resize(n, 1e9 + 1);
        tree.resize(2 * n);

        for (int i = 2 * n - 1; i >= 1; --i)
        {
            if (i >= n)
                tree[i] = {arr[i - n], 1};
            else
            {
                long long mini = min(tree[2 * i][0], tree[2 * i + 1][0]), count = 0;

                if (tree[2 * i + 1][0] == mini)
                {
                    count += tree[2 * i + 1][1];
                }

                if (tree[2 * i][0] == mini)
                {
                    count += tree[2 * i][1];
                }

                tree[i] = {mini, count};
            }
        }
    }

    void mini(int l, int r)
    {
        l += n;
        r += n;

        vector<vector<long long>> candidates;

        while (l <= r)
        {
            if (l % 2 == 1)
                candidates.push_back(tree[l++]);

            if (r % 2 == 0)
                candidates.push_back(tree[r--]);

            l /= 2;
            r /= 2;
        }

        long long mini = 1e9 + 1, count = 0;
        for (auto x : candidates)
        {
            if (x[0] < mini)
            {
                mini = x[0];
                count = 0;
            }

            if (mini == x[0])
                count += x[1];
        }

        cout << mini << " " << count << endl;
    }

    void set(int i, int v)
    {
        i += n;
        tree[i] = {v, 1};

        for (i /= 2; i >= 1; i /= 2)
        {
            long long mini = min(tree[2 * i][0], tree[2 * i + 1][0]), count = 0;

            if (tree[2 * i + 1][0] == mini)
            {
                count += tree[2 * i + 1][1];
            }

            if (tree[2 * i][0] == mini)
            {
                count += tree[2 * i][1];
            }

            tree[i] = {mini, count};
        }
    }
};

int main()
{
    int n, m;
    cin >> n >> m;

    vector<long long> arr(n);
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
            st.mini(a, b - 1);
    }
}