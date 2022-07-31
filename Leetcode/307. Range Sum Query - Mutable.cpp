/**
 * https://leetcode.com/problems/range-sum-query-mutable/
 * Time: O(N), O(NlogN), O(NlogN)
 * Space: O(N)
 */

class NumArray {
public:
    int n = 1;
    vector<int> tree;

    NumArray(vector<int> &nums) {

        int l = nums.size();
        while (n < l)
            n <<= 1;
        nums.resize(n);
        tree.resize(2 * n);

        for (int i = 2 * n - 1; i > 0; --i) {
            if (i < n)
                tree[i] = tree[2 * i] + tree[2 * i + 1];
            else
                tree[i] = nums[i - n];
        }
    }

    void update(int index, int val) {

        index += n;
        tree[index] = val;

        for (index /= 2; index > 0; index /= 2)
            tree[index] = tree[2 * index] + tree[2 * index + 1];
    }

    int sumRange(int left, int right) {

        left += n, right += n;
        int res = 0;

        while (left <= right) {
            if (left & 1)
                res += tree[left++];
            if ((!(right & 1)))
                res += tree[right--];
            left /= 2, right /= 2;
        }

        return res;
    }
};