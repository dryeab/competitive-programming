/**
 * https://leetcode.com/problems/find-all-anagrams-in-a-string/
 * Time: O(n)
 * Space: O(n)
 */

class Solution {
public:
    vector<int> findAnagrams(string s, string p) {

        int n = s.size(), m = p.size();
        vector<int> res, cnt(26);

        for (char c : p)
            ++cnt[c - 'a'];

        for (int i = 0, j = 0; i < n && j < n; ++i) {
            while (j < n && j - i < m)
                --cnt[s[j++] - 'a'];

            bool ok = true;
            for (int k : cnt) {
                if (k) {
                    ok = false;
                    break;
                }
            }

            if (ok)
                res.push_back(i);

            cnt[s[i] - 'a']++;
        }

        return res;
    }
};