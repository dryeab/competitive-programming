/**
 * https://leetcode.com/problems/longest-consecutive-sequence/
 * Time: O(n)
 * Space: O(n)
 */

class Solution {
public:
    int longestConsecutive(vector<int> &nums) {

        unordered_set<int> elements;
        for (int num : nums)
            elements.insert(num);

        int res = 0, cur;
        for (int num : elements) {
            if (!elements.count(num - 1)) {
                cur = 0;
                while (elements.count(num)) {
                    cur++;
                    num++;
                }
                res = max(res, cur);
            }
        }

        return res;
    }
};