#include <iostream>
#include <vector>

using namespace std;

struct segment_tree
{
    int n;
    vector<long long> tree;

    void init(vector<long long> &arr)
    {
        n = 1;
        while (n < arr.size())
            n *= 2;

        arr.resize(n, 0);
        tree.resize(2 * n, 0);

        for (int i = 2 * n - 1; i >= 1; --i)
        {
            if (i >= n)
                tree[i] = arr[i - n];
            else
                tree[i] = tree[2 * i] + tree[2 * i + 1];
        }
    }

    long long sum(int l, int r)
    {
        l += n;
        r += n;

        long long res = 0;
        while (l <= r)
        {
            if (l % 2 == 1)
                res += tree[l++];
            if (r % 2 == 0)
                res += tree[r--];
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
            tree[i] = tree[2 * i] + tree[2 * i + 1];
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
            cout << st.sum(a, b - 1) << endl;
    }
}