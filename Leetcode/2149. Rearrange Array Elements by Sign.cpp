/*
    https://leetcode.com/problems/rearrange-array-elements-by-sign/
    Time: O(n)
    Space: O(n)
*/

class Solution {
public:
    vector<int> rearrangeArray(vector<int> &nums) {

        int pos = 0, neg = 0, turn = 1;
        vector<int> res;

        while (res.size() < nums.size()) {
            if (turn == 1) {
                while (nums[pos] < 0)
                    pos++;
                res.push_back(nums[pos]);
                pos++;
            } else {
                while (nums[neg] > 0)
                    neg++;
                res.push_back(nums[neg]);
                neg++;
            }
            turn = (turn + 1) % 2;
        }

        return res;
    }
};