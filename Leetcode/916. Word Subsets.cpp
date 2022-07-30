/**
 * https://leetcode.com/problems/word-subsets/
 * Time: O(N + M)
 * Space: O(N + M)
 */

class Solution {
public:
    vector<string> wordSubsets(vector<string>& words1, vector<string>& words2) {
     
        vector<int> maxCount(26);
        
        for (string word: words2){
            vector<int> cnt(26);
            for (char c: word)
                cnt[c - 'a']++;
            for (int i = 0; i < 26; ++i)
                maxCount[i] = max(maxCount[i], cnt[i]);
        }
        
        vector<string> res;
        
        for (string word: words1){
            vector<int> cnt(26);
            for (char c: word)
                cnt[c - 'a']++;
            bool ok = true;
            for (int i = 0; i < 26 && ok; ++i)
                ok = cnt[i] >= maxCount[i];
            
            if (ok)
                res.push_back(word);
        }
        
        return res;
    }
};