#include <iostream>
#include <vector>

using namespace std;

/*
    Note:
        -> Increment n to the nearest power of two
        -> Make the tree size 2n and put the root at index 1 so that indexing will be easier
        -> Left child is always at even index
        -> Right child is always at odd index
        -> Make sure the sum's limit is `long long` to make sufficient room for large numbers
*/

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
    // Sample test

    vector<long long> arr = {1, 2, 3, 4, 5, 6};

    segment_tree st;
    st.init(arr);

    int l, r;
    cin >> l >> r;

    cout << "The sum is " << st.sum(l, r) << endl;
}